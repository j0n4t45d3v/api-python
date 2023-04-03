class User:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'age': self.age}

    @property
    def name_user(self):
        return self.name

    @name_user.setter
    def name_user(self, name):
        self.name = name

    @property
    def age_user(self):
        return self.name

    @age_user.setter
    def age_user(self, name):
        self.name = name
