class Rectangle:
    def __init__(self, width, height):
        self.rectangle_width = width
        self.rectangle_height = height
    
    def calculator_area(self):
        rectangle_area = self.rectangle_height * self.rectangle_width
        return rectangle_area
    
    def calculate_perimeter(self):
        rectangle_perimeter = 2 * (self.rectangle_width * self.rectangle_height)
        return rectangle_perimeter
# Tie class to a variable
width = 45 # insert value here
height = 30 # insert value here
rect = Rectangle(width, height)

# Tie functions to a variable
calculated_area = rect.calculator_area()
calculated_perimeter = rect.calculate_perimeter()

# Print out information
print(f"The area of the rectangle is {calculated_area}")
print(f"The perimeter of the rectangle is {calculated_perimeter})