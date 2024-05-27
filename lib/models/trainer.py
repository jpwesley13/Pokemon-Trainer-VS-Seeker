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
        
    @property
    def hometown(self):
        return self._hometown
    
    @hometown.setter
    def hometown(self, hometown):
        if isinstance(hometown, str) and len(hometown):
            self._hometown = hometown
        else:
            raise ValueError("Please enter a non-empty string for the trainer's hometown")
        
    @property
    def badges(self):
        return self._badges
    
    @badges.setter
    def badges(self, badges):
        if isinstance(badges, int) and 0 <= badges <= 8:
            self._badges = badges
        else:
            raise ValueError("Please enter an integer between 0 and 8 for the trainer's badge count")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS trainers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            hometown TEXT,
            badges INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS departments;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO trainers (name, hometown, badges)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.hometown, self.badges))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self