import copy
from classes import Rectangle
from classes import Parallelepiped

# Creating instances of Rectangle
rectangle1 = Rectangle()
rectangle2 = Rectangle(5, 5)

# Creating a copy of rectangle2
rectangle3 = copy.copy(rectangle2)

# Displaying details of rectangles
print("Rectangle 1 Details:")
print(rectangle1.to_string())
print(f"Perimeter: {rectangle1.perimeter()}")
print(f"Area: {rectangle1.area()}\n")

print("Rectangle 2 Details:")
print(rectangle2.to_string())
print(f"Perimeter: {rectangle2.perimeter()}")
print(f"Area: {rectangle2.area()}\n")

print("Rectangle 3 Details:")
print(rectangle3.to_string())
print(f"Perimeter: {rectangle3.perimeter()}")
print(f"Area: {rectangle3.area()}\n")

# Checking equality between rectangles
print("Equality Check for Rectangles:")
print("Rectangle 1 and Rectangle 2 are equal:", rectangle1.equals(rectangle2))
print("Rectangle 2 and Rectangle 3 are equal:", rectangle2.equals(rectangle3),"\n")


# Creating instances of Parallelepiped
parallelepiped1 = Parallelepiped(2, 3, 4)
parallelepiped2 = Parallelepiped(3, 3, 3)

# Displaying details of parallelepipeds
print("Parallelepiped 1 Details:")
print(parallelepiped1.to_string())
print(f"Perimeter: {parallelepiped1.perimeter()}")
print(f"Surface Area: {parallelepiped1.surface_area()}")
print(f"Volume: {parallelepiped1.volume()}\n")

print("Parallelepiped 2 Details:")
print(parallelepiped2.to_string())
print(f"Perimeter: {parallelepiped2.perimeter()}")
print(f"Surface Area: {parallelepiped2.surface_area()}")
print(f"Volume: {parallelepiped2.volume()}\n")


# Checking equality between parallelepipeds
print("Equality Check for Parallelepipeds:")
print("Parallelepiped 1 and Parallelepiped 2 are equal:", parallelepiped1.equals(parallelepiped2))
