from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dinosaur1 = Dinosaur("Trex", 4)
        dinosaur2 = Dinosaur("Triceratops", 3)
        dinosaur3 = Dinosaur("Velociraptor", 2)
        self.dinosaurs.append(dinosaur1)
        self.dinosaurs.append(dinosaur2)
        self.dinosaurs.append(dinosaur3)
