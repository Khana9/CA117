#!/usr/bin/env python3

class Point():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x:.1f}, {self.y:.1f})"

    def distance(self, p2):
        return (((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2) ** 0.5)
