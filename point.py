import math

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from(self, p):
        return math.sqrt((self.x - p.x)**2.0 + (self.y - p.y)**2.0)

    def print_point(self):
        print('({0}, {1})'.format(self.x, self.y))