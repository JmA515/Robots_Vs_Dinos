from robot import Robot

class Fleet:
    def __init__(self):
        self.robots =  []
        self.create_fleet()

    def create_fleet(self):
        robot1 = Robot("Bob")
        robot2 = Robot("Bob2.0")
        robot3 = Robot("Omega Bob")
        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)