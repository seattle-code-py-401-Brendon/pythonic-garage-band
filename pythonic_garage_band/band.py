
class Band:
    def __init__(self, name, members=None, instances=[]):
        self.name = name
        self.members = members
        self.instances = instances
        Band.instances.append(self)
    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"
    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos

    @classmethod
    def to_list(cls):
        return cls.instances
        


class Musician():
    pass

class Guitarist(Musician, Band):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(cls):
        return f"guitar"
    def play_solo(cls):
        return f"face melting guitar solo"

class Bassist(Musician,Band):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"My name is {self.name} and I play bass"
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
    def get_instrument(cls):
        return f"bass"
    def play_solo(cls):
        return f"bom bom buh bom"

class Drummer(Musician,Band):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"My name is {self.name} and I play drums"
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    def get_instrument(cls):
        return f"drums"
    def play_solo(cls):
        return f"rattle boom crash"
    