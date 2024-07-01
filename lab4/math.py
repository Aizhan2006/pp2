#1 Write a Python program to convert degree to radian
import math

def degree_to_radian(degree):
    radian = degree * (math.pi / 180)
    return radian

# Example 
degree = 15
radian = degree_to_radian(degree)
print(radian)


#2 Write a Python program to calculate the area of a trapezoid.
def area_of_trapezoid(height, base1, base2):
    area = ((base1 + base2) / 2) * height
    return area

# Example 
height = 5
base1 = 5
base2 = 6
area = area_of_trapezoid(height, base1, base2)
print(area)


#3 Write a Python program to calculate the area of regular polygon.
import math

def area_of_polygon(num_sides, side_length):
    area = (num_sides * (side_length ** 2)) / (4 * math.tan(math.pi / num_sides))
    return area

# Example 
num_sides = 5
side_length = 25
area = area_of_polygon(num_sides, side_length)
print(area)


#4 Write a Python program to calculate the area of a parallelogram.
def area_of_parallelogram(base, height):
    area = base * height
    return area

# Example usage:
base = 5
height = 6
area = area_of_parallelogram(base, height)
print(area)

