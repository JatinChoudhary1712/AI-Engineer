from abstract_class import vehicle

class Bike(vehicle):
    def __init__(self, n , colour):
        self.colour = colour
        super().__init__(n)
    def start(self):
        print("Start with kick ")


class Scooty(vehicle):
    def __init__(self, n):
        super().__init__(n)
    def start(self):
        print("start with self start")
        
class Car(vehicle):
    def __init__(self, n):
        super().__init__(n)
    def start(self):
        print("start with key")