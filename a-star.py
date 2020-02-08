import math
from point import Point
from node import Node


openlist = []
closedlist = []

def build_nodes(val):
    for row in val:
        for col in row:
            print(col, end ='\t')
        print('\n')

T = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

p1 = Point(6, 7)
p2 = Point(2, 3)

p1.print_point()
p2.print_point()

print(p1.distance_from(p2))

for row in T:
    for col in row:
        print(col, end ='\t')
    print('\n')
        
def create_nodes():
    for row in T:
        for col in row:
            
            

"""
G-cost: distance from starting node
H-cost: distance from end node
F-cose: G-cost + H-cost
"""