import numpy as np

class Circle:

    def __init__(self,radius):
        self.radius = radius

    def perimeter(self):
        return 2*np.pi*self.radius

    def area(self):
        return np.pi*self.radius**2

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        if self.radius == other.radius or self.radius > other.radius:
            return ""
        
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius