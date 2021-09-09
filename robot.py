from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.weapon = Weapon("laser", 2)

    def attack(self, dinosaur):
        dinosaur.health = dinosaur.health - self.weapon.attack_power
        print(f'{self.name} deals {self.weapon.attack_power} damage to {dinosaur.name}')
        print(f'{dinosaur.name} is down to {dinosaur.health} health')
