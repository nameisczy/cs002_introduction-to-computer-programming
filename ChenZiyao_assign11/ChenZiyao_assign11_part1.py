class Rectangle:
    def __init__(self, width, length, x, y):
        self.width = width
        self.length = length
        self.x = x
        self.y = y
    def get_area(self):
        return self.width * self.length
    def get_perimeter(self):
        return 2 * self.length + 2 * self.width

'''
Rectangle #1
* Coordinates: (5, 3)
* Area: 150
* Perimeter: 50

Rectangle #2
* Coordinates: (15, 7)
* Area: 15
* Perimeter: 16
'''

Rectangle1 = Rectangle(10, 15, 5, 3)
print("Rectangle #1")
print("* Coordinates:", (Rectangle1.x, Rectangle1.y))
print("* Area:", Rectangle1.get_area())
print("* Perimeter:", Rectangle1.get_perimeter())
print()
Rectangle2 = Rectangle(3, 5, 15, 7)
print("Rectangle #2")
print("* Coordinates:", (Rectangle2.x, Rectangle2.y))
print("* Area:", Rectangle2.get_area())
print("* Perimeter:", Rectangle2.get_perimeter())
