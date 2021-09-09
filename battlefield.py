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
        print("Welcome to Robots Vs Dinosaurs!")

    def battle(self):
        pass

    def dino_turn(self, dinosaur):
        dinosaur.attack(random.choice(self.fleet.robots))

    def robo_turn(self, robot):
        robot.attack(random.choice(self.herd.dinosaurs))

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winner(self):
        pass
