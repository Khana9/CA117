#!/usr/bin/env python3

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x:.1f}, {self.y:.1f})'

    def midpoint(self, other):
        tmp_x = (self.x + other.x) / 2
        tmp_y = (self.y + other.y) / 2
        return Point(tmp_x, tmp_y)
