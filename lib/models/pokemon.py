import json
from models.__init__ import CURSOR, CONN
from models.trainer import Trainer

with open("lib/kanto.json") as file:
    kanto_list = json.load(file)

class Pokemon:
    all = {}

    def __init__(self, nickname, species, level, trainer, id=None):
        self.id = id
        self.nickname = nickname
        self.species = species
        self.level = level
        self.trainer = trainer
        #Pokemon.all.append(self)

    def __repr__(self):
        return f"{self.nickname}"
    
    def details(self):
        return (
            f"{self.trainer} has caught this Pokemon: \n" +
            f"{self.nickname} the {self.species}. Level {self.level}"
            )

    @property
    def nickname(self):
        return self._nickname
    
    @nickname.setter
    def nickname(self, nickname):
        if isinstance(nickname, str) and len(nickname):
            self._nickname = nickname
        else:
            raise ValueError("Please enter a non-empty string for the Pokemon's nickname")

    @property
    def species(self):
        return self._species
    
    @species.setter
    def species(self, species):
        if species not in kanto_list:
            raise Exception("Please enter a Kantonian Pokemon species")
        self._species = species

    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, level):
        if isinstance(level, int) and 1 <= level <= 100:
            self._level = level
        else:
            raise ValueError("Please enter an integer between 1 and 100 for the Pokemon's level")
        
    @property
    def trainer(self):
        return self._trainer
    
    @trainer.setter
    def trainer(self, trainer):
        if type(trainer) is str and Trainer.find_by_name(trainer):
            self._trainer = trainer
        else:
            raise ValueError("trainer must reference an existing Trainer name in the database")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS pokemons (
            id INTEGER PRIMARY KEY,
            nickname TEXT,
            species TEXT,
            level INTEGER,
            trainer TEXT,
            FOREIGN KEY (trainer) REFERENCES trainers(name))
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
            INSERT INTO pokemons (nickname, species, level, trainer)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.nickname, self.species, self.level, self.trainer))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE pokemons
            SET nickname = ?, species = ?, level = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.nickname, self.species, self.level, self.id))
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
    def create(cls, nickname, species, level, trainer):
        pokemon = cls(nickname, species, level, trainer)
        pokemon.save()
        return pokemon
    
    @classmethod
    def instance_from_db(cls, row):
        pokemon = cls.all.get(row[0])
        if pokemon:
            pokemon.nickname = row[1]
            pokemon.species = row[2]
            pokemon.level = row[3]
            pokemon.trainer = row[4]
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
    
    @classmethod
    def find_by_nickname(cls, nickname):
        sql = """
            SELECT *
            FROM pokemons
            WHERE nickname is ?
        """
        row = CURSOR.execute(sql, (nickname,)).fetchone()
        return cls.instance_from_db(row) if row else None
    