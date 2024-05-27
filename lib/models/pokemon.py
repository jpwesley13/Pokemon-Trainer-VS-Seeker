import json
import ipdb
from __init__ import CURSOR, CONN
from trainer import Trainer

with open("lib/kanto.json") as file:
    kanto_list = json.load(file)

class Pokemon:
    all = {}

    def __init__(self, nickname, species, level, trainer):
        self.nickname = nickname
        self.species = species
        self.level = level
        self.trainer = trainer
        #Pokemon.all.append(self)

    def __repr__(self):
        return(
            f"<{self.species}. Nickname: {self.nickname}, Level: {self.level}, " +
            f"Trainer Name: {self.trainer}>"
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
            

ipdb.set_trace()