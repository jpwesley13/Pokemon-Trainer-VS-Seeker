import json
from __init__ import CURSOR, CONN
from trainer import Trainer

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
        return(
            f"<{self.id}. {self.species}. Nickname: {self.nickname}, "
            f"Level: {self.level}, Trainer Name: {self.trainer}>"
        )

    @property
    def nickname(self):
        return self._nickname
    
    @nickname.setter
    def nickname(self, nickname):
        if isinstance(nickname, str) and not hasattr(self, "nickname") and len(nickname):
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
        if isinstance(level, str) and 1 <= level <= 100:
            self._level = level
        else:
            raise ValueError("Please enter an integer between 1 and 100 for the Pokemon's level")
        
    @property
    def trainer(self):
        return self._trainer
    
    @trainer.setter
    def trainer(self, trainer):
        if isinstance(trainer, str) and Trainer.find_by_name(trainer):
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

    