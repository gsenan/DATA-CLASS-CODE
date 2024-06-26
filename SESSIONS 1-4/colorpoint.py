from classexample import Point
import random

a = Point(5, 5)
print(a)

class ColorPoint(Point):
    # This is a class that inherits from Point!
    COLORS = ["red", "blue", "green", "yellow", "purple", "cyan", "black", "white", "celadon", "xanadoo"]
    def __init__(self, x, y, color):
        # self.x = x
        # self.y = y
        super().__init__(x, y) # Calling the parent init method.
        if color in self.COLORS:
            self.color = color
        else:
            raise Exception(f"This is an unsupported color. Allowed colors are: {self.COLORS}")

    @classmethod
    def add_extra_color(cls, color):
        """
        Add a new valid color to the list.
        :param color: The name of the color to add.
        """
        cls.COLORS.append(color)

    @property
    def distance_orig(self):
        """
        Return distance from origin of the point instance.
        :return:
        """
        return (self.x**2 + self.y**2)**0.5

    def __str__(self):
        return f"{self.color}<{self.x}, {self.y}"

if __name__ == "__main__":
    # we added this if to not show all the below lines when importing into advanced point
    red_point = ColorPoint(10, 10, "red")
    ColorPoint.add_extra_color("orange")
    orange_point = ColorPoint(20, 20, "orange")
    red_point.x = 30
    # print(f"{red_point} has distance to origin = {red_point.distance_orig()}") # before it was a property
    print(f"{red_point} has distance to origin = {red_point.distance_orig}") # after it was a property

# Let's do 5 random color points
colors = ["red", "blue", "green", "yellow", "purple", "cyan", "black", "white", "celadon", "xanadoo"]
color_points = []
for _ in range(5):
    color_point = ColorPoint(random.randint(1, 100), random.randint(1, 100), random.choice(colors))
    color_points.append(color_point)

print(color_points)