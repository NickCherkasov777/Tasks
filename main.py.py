# main.py

from areas import rectangle_area, triangle_area, circle_area

def main():
    """
    Main function to get user input and calculate the area of a chosen shape.
    """
    print("Which figure's area do you want to calculate?")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = input("Enter the number of your choice (1, 2, or 3): ")

    if choice == '1':
        try:
            length = float(input("Enter the length of the rectangle (a): "))
            width = float(input("Enter the width of the rectangle (b): "))
            area = rectangle_area(length, width)
            print(f"The area of the rectangle is: {area}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
    elif choice == '2':
        try:
            height = float(input("Enter the height of the triangle (h): "))
            base = float(input("Enter the base of the triangle (a): "))
            area = triangle_area(height, base)
            print(f"The area of the triangle is: {area}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
    elif choice == '3':
        try:
            radius = float(input("Enter the radius of the circle (r): "))
            area = circle_area(radius)
            print(f"The area of the circle is: {area}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()