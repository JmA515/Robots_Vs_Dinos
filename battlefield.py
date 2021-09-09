from fleet import Fleet
from herd import Herd
import random

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()

    def display_welcome(self):
        print("Welcome to Robots Vs Dinosaurs!\nLet the battle begin!")

    def battle(self):
        all_dinos_defeated = False
        all_robos_defeated = False
        turn_count = 1
        while all_dinos_defeated != True and all_robos_defeated != True:
            self.robo_turn(random.choice(self.fleet.robots))
            all_dinos_defeated = self.show_dino_opponent_options()
            self.dino_turn(random.choice(self.herd.dinosaurs))
            all_robos_defeated = self.show_robo_opponent_options()
            print(f'Turn {turn_count}')
            turn_count += 1
        if all_dinos_defeated == True:
            return "Robots Win!"
        if all_robos_defeated == True:   
            return "Dinosaurs Win!"

    def dino_turn(self, dinosaur):
        dinosaur.attack(random.choice(self.fleet.robots))

    def robo_turn(self, robot):
        robot.attack(random.choice(self.herd.dinosaurs))

    def show_dino_opponent_options(self):
        print(f'{self.herd.dinosaurs[0].name} has {self.herd.dinosaurs[0].health} health')
        print(f'{self.herd.dinosaurs[1].name} has {self.herd.dinosaurs[1].health} health')
        print(f'{self.herd.dinosaurs[2].name} has {self.herd.dinosaurs[2].health} health')
        if self.herd.dinosaurs[0].health <= 0 and self.herd.dinosaurs[1].health <= 0 and self.herd.dinosaurs[2].health <= 0:
            return True

    def show_robo_opponent_options(self):
        print(f'{self.fleet.robots[0].name} has {self.fleet.robots[0].health} health')
        print(f'{self.fleet.robots[1].name} has {self.fleet.robots[1].health} health')
        print(f'{self.fleet.robots[2].name} has {self.fleet.robots[2].health} health')
        if self.fleet.robots[0].health <= 0 and self.fleet.robots[1].health <= 0 and self.fleet.robots[2].health <= 0:
            return True

    def display_winner(self):
        pass
