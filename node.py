from point import Point
"""
Each node represents one square grid on the field
A Node is either walkable or not
"""
class Node:
    # G-cost: distance from starting node
    # H-cost: distance from end node
    # F-cose: G-cost + H-cost

    def __init__(self, walkable, position):
        self.walkable = walkable
        self.position = position

    def display_cost(self):
        print(self.G, self.H, self.F)

    def calc_values(self, parent, start, end):
        if self.walkable:
            self.parent = parent
            self.G = self.position.distance_from(start)
            self.H = self.position.distance_from(end)
            self.F = self.G + self.H