import json
import ipdb

with open("lib/kanto.json") as file:
    kanto_list = json.load(file)

class Pokemon:
    all = []

    def __init__(self, nickname, species, level, trainer):
        self.nickname = nickname
        self.species = species
        self.level = level
        self.trainer = trainer
        Pokemon.all.append(self)

    @property
    def species(self):
        return self._species
    
    @species.setter
    def species(self, species):
        if species not in kanto_list:
            raise Exception("Please enter a Kantonian Pokemon species")
        self._species = species

ipdb.set_trace()