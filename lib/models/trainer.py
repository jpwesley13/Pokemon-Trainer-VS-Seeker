from models.__init__ import CURSOR, CONN

class Trainer:

    all = {}

    def __init__(self, name, hometown, badges, id=None):
        self.id = id
        self.name  = name
        self.hometown = hometown
        self.badges = badges

    def __repr__(self):
        return f"<Trainer {self.id}: {self.name} from {self.hometown}, {self.badges} badge(s)>"
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Please enter a non-empty string for the trainer name")