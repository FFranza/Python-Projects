# Classes and Function Practice excercise 1: Calculator
# Uses a class to organize a group of functions
class Calculator:
    def addition(self, x, y): # Addition function
        sum = x + y
        return sum
    
    def subtraction(self, x, y): # Subtraction function
        difference = x - y
        return difference
    
    def division(self, x, y): # Division function
        if y != 0: # Checks so that y can not be 0
            quotient = x / y
            return quotient
        else:
            return "Division by zero is not allowed"
    
    def multipication(self, x, y): # Multiplication function
        product = x * y 
        return product

# Input values here
x = # Input Number here for X
y = # Input Number here for Y
# Ties the Calculator class to a variable to allowing calling
calc = Calculator()
# Ties variable that contains the class and allows for calling the class and the specific function (classvariable.functioninsideclass)
add_result = calc.addition(x, y) 
subtract_result = calc.subtraction(x, y)
divide_result = calc.division(x, y)
multiply_result = calc.multipication(x, y)
# Print values
print(add_result)
print(subtract_result)
print(divide_result)
print(multiply_result)