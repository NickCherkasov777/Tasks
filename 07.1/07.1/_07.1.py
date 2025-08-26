# 07.1 Practical tasks

# Task 1

def max_of_two(a, b):
    """
    Returns the largest of two numbers.

    Parameters:
    a (int or float): First number
    b (int or float): Second number

    Returns:
    int or float: The larger number between a and b
    """
    return a if a > b else b

# приклад використання
print(max_of_two(10, 20))  # 20
print(max_of_two(7, 3))    # 7

# Task 2

import math

def rectangle_area(length, width):
    """Return area of a rectangle."""
    return length * width

def triangle_area(base, height):
    """Return area of a triangle."""
    return 0.5 * base * height

def circle_area(radius):
    """Return area of a circle."""
    return math.pi * radius ** 2

# головна програма
print("Choose shape: rectangle, triangle, circle")
choice = input("Enter shape: ").lower()

if choice == "rectangle":
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print("Area of rectangle:", rectangle_area(l, w))

elif choice == "triangle":
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print("Area of triangle:", triangle_area(b, h))

elif choice == "circle":
    r = float(input("Enter radius: "))
    print("Area of circle:", circle_area(r))

else:
    print("Invalid choice")

# Task 3

def count_characters(s):
    """
    Count the frequency of each character in a string.

    Parameters:
    s (str): Input string

    Returns:
    dict: Dictionary with characters as keys and counts as values
    """
    result = {}
    for ch in s:
        result[ch] = result.get(ch, 0) + 1
    return result


# приклад використання
print(count_characters("hello"))
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}


