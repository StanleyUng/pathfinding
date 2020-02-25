from point import Point
from enum import Enum


class NodeType(Enum):
    EMPTY = 0
    WALL = 1
    START = 2
    END = 3


"""
Each node represents one square grid on the field
A Node is either walkable or not
"""
class Node:
    # G-cost: distance from starting node
    # H-cost: distance from end node
    # F-cose: G-cost + H-cost

    def __init__(self, walkable, position):
        self.G = 0
        self.H = 0
        self.F = 0
        self.walkable = walkable
        self.position = position
        self.type = NodeType.EMPTY
        self.color = (255, 255, 255) # white

    def display_cost(self):
        print('(G: {0}, H: {1} F:{2})'.format(self.G, self.H, self.F))

    def calc_values(self, start, end):
        if self.walkable:
            # self.parent = parent
            self.G = self.position.distance_from(start)
            self.H = self.position.distance_from(end)
            self.F = self.G + self.H