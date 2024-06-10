import json
from models.__init__ import CURSOR, CONN
from models.trainer import Trainer

with open("lib/kanto.json") as file:
    kanto_list = json.load(file)

class Pokemon:
    all = {}

    def __init__(self, name, species, level, trainer_id, id=None):
        self.id = id
        self.name = name
        self.species = species
        self.level = level
        self.trainer_id = trainer_id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Please enter a non-empty string for the Pokemon's nickname\n")

    @property
    def species(self):
        return self._species
    
    @species.setter
    def species(self, species):
        if species not in kanto_list:
            raise Exception("Please enter a Kantonian Pokemon species\n")
        self._species = species

    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, level):
        if isinstance(level, int) and 1 <= level <= 100:
            if hasattr(self, "_level") and level < self._level:
                raise ValueError("New level must not be lower than the current level\n")
            self._level = level
        else:
            raise ValueError("Please enter an integer between 1 and 100 for the Pokemon's level\n")
        
    @property
    def trainer_id(self):
        return self._trainer_id
    
    @trainer_id.setter
    def trainer_id(self, trainer_id):
        if type(trainer_id) is int and Trainer.find_by_id(trainer_id):
            self._trainer_id = trainer_id
        else:
            raise ValueError("trainer must reference an existing Trainer ID in the database\n")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS pokemons (
            id INTEGER PRIMARY KEY,
            name TEXT,
            species TEXT,
            level INTEGER,
            trainer_id INTEGER,
            FOREIGN KEY (trainer_id) REFERENCES trainers(id))
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS pokemons;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO pokemons (name, species, level, trainer_id)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.species, self.level, self.trainer_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE pokemons
            SET name = ?, species = ?, level = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.species, self.level, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM pokemons
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, name, species, level, trainer_id):
        pokemon = cls(name, species, level, trainer_id)
        pokemon.save()
        return pokemon
    
    @classmethod
    def instance_from_db(cls, row):
        pokemon = cls.all.get(row[0])
        if pokemon:
            pokemon.name = row[1]
            pokemon.species = row[2]
            pokemon.level = row[3]
            pokemon.trainer_id = row[4]
        else:
            pokemon = cls(row[1], row[2], row[3], row[4])
            pokemon.id = row[0]
            cls.all[pokemon.id] = pokemon
        return pokemon
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM pokemons
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM pokemons
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    