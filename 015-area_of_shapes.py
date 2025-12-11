
import math
class AreaOfShapes:
    def __init__(self, length=1, width=1,base=1, height=1, radius=1):
        self.length = length
        self.width = width
        self.base = base
        self.height = height
        self.radius = radius
    
    def SquareArea(self):
        return self.length ** 2
    
    def RectangleArea(self):
        return self.length * self.width
    
    def TriangleArea(self):
        return (self.base * self.height)/2
    
    def CircleArea(self):
        return math.pi * (self.radius**2)

user = AreaOfShapes(5, 4, 8, 3, 9)
print(f"Area of Square = {user.SquareArea()}")
print(f"Area of Rectangle = {user.RectangleArea()}")
print(f"Area of Triangle = {user.TriangleArea()}")
print(f"Area of Circle = {user.CircleArea()}")