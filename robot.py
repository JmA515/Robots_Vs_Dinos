from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.weapon = Weapon()

    def attack(self, dinosaur):
        pass