from models.__init__ import CURSOR, CONN

class Trainer:

    all = {}

    def __init__(self, name, hometown, badges, id=None):
        self.id = id
        self.name  = name
        self.hometown = hometown
        self.badges = badges

    def __repr__(self):
        return f"{self.name}"
    
    def details(self):
        return f"{self.name} from {self.hometown}. Currently has {self.badges} badge(s) and {len(self.pokemons())} Pokemon!"
    
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
            DROP TABLE IF EXISTS trainers;
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

    @classmethod
    def create(cls, name, hometown, badges):
        trainer = cls(name, hometown, badges)
        trainer.save()
        return trainer
    
    def update(self):
        sql = """
            UPDATE trainers
            SET name = ?, badges = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.badges, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM trainers
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        trainer = cls.all.get(row[0])
        if trainer:
            trainer.name = row[1]
            trainer.hometown = row[2]
            trainer.badges = row[3]
        else:
            trainer = cls(row[1], row[2], row[3])
            trainer.id = row[0]
            cls.all[trainer.id] = trainer
        return trainer
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM trainers
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM trainers
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    # @classmethod
    # def find_by_name(cls, name):
    #     sql = """
    #         SELECT *
    #         FROM trainers
    #         WHERE name is ?
    #     """
    #     row = CURSOR.execute(sql, (name,)).fetchone()
    #     return cls.instance_from_db(row) if row else None
    
    def pokemons(self):
        from models.pokemon import Pokemon
        sql = """
            SELECT *
            FROM pokemons
            WHERE trainer = ?
        """
        CURSOR.execute(sql, (self.id,),)
        rows = CURSOR.fetchall()
        return [Pokemon.instance_from_db(row) for row in rows]