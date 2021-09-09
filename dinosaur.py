class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 5

    def attack(self, robot):
        if robot.health >= 0:
            robot.health = robot.health - self.attack_power
            print(f'{self.name} deals {self.attack_power} damage to {robot.name}')
            print(f'{robot.name} is down to {robot.health} health')
        else:
            print("That opponent is already defeated.")