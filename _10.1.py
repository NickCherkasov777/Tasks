class Polygon:
    """A base class for polygons."""
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    """
    A class for a rectangle, inheriting from Polygon.
    Calculates the area (square) of the rectangle.
    """
    def __init__(self, length, width):
        # Call the parent class constructor
        super().__init__(4)  # A rectangle has 4 sides
        self.length = length
        self.width = width

    def get_area(self):
        """Calculates the area of the rectangle."""
        return self.length * self.width

# Example usage for Task 1
rect = Rectangle(10, 5)
print(f"The area of the rectangle is: {rect.get_area()}")

class Human:
    """A class to represent a human being."""
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        """Displays a welcome message for the human."""
        print(f"Welcome, {self.name}!")

    def get_species(self):
        """Returns the species of the human."""
        return f"This person is a species of \"{self.species}\"."

    @staticmethod
    def arbitrary_message():
        """Returns an arbitrary message."""
        return "This is a static message from the Human class."

# Example usage for Task 2
person = Human("Alice")
person.welcome_message()
print(person.get_species())
print(Human.arbitrary_message())

class Employee:
    """
    An employee class with a counter for the total number of employees.
    """
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def display_employee_info(self):
        """Displays the name and salary of the employee."""
        print(f"Name: {self.name}, Salary: ${self.salary}")

    @classmethod
    def print_total_employees(cls):
        """Prints the total number of employees."""
        print(f"Total number of employees: {cls.total_employees}")

# Example usage for Task 3
emp1 = Employee("Bob", 60000)
emp2 = Employee("Charlie", 75000)

emp1.display_employee_info()
emp2.display_employee_info()
Employee.print_total_employees()

# Displaying class information
print("\n--- Employee Class Metadata ---")
print(f"Base classes: {Employee.__bases__}")
print(f"Class namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation bar: {Employee.__doc__}")