# part 1 

print("=== PART 1: BASIC FUNCTIONS ===")

# Example 1: Simple function without parameters
def say_hello():
    """A simple function that prints a greeting"""
    print("Hello, World!")
    print("Welcome to Python functions!")

# Calling the function
print("Calling say_hello():")
say_hello()
print()



#Part 2 Function with one parameter

def greet_person(name):
    """Greets a person by name"""
    print(f"Hello, {name}! Nice to meet you.")

print("Calling greet_person with different names:")
greet_person("Alice")
greet_person("Bob")
greet_person("Charlie")
print()



#part 3
# Example 1: Function that returns a value
def number(n, b):
    result = n + b
    return

print("Functions return value:")
sum1 = number(5,3)
sum2 = number(10,7) 
print(f"5 + 3 = {sum1} ")
print(f"10 + 7 = {sum2} ")
print(f"Sum of both results: {sum1 + sum2}")
print()

#คำตอบ
def add_numbers(a, b):
    """Adds two numbers and returns the result"""
    result = a + b
    return result

print("Using functions that return values:")
sum1 = add_numbers(5, 3)
sum2 = add_numbers(10, 7)
print(f"5 + 3 = {sum1}")
print(f"10 + 7 = {sum2}")
print(f"Sum of both results: {sum1 + sum2}")
print()




# Example 2: Function returning multiple values
def get_circle_info(radius):
    """Calculates circle area and circumference"""
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return area, circumference

print("Circle calculations:")
radius = 5
area, circumference = get_circle_info(radius)
print(f"Circle with radius {radius}:")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
print()



#part 4 
# Example 1: Function with default parameter
def greet_with_title(name, title="Mr./Ms."):
    """Greets person with optional title"""
    print(f"Hello, {title} {name}!")

print("Using default parameters:")
greet_with_title("Smith")  
greet_with_title("Johnson", "Dr.")  
greet_with_title("Brown", "Prof.")  
print()




# Example 2: Multiple default parameters
def create_profile(name, age=18, country="Unknown"):
    """Creates a user profile with default values"""
    print(f"Profile: {name}, Age: {age}, Country: {country}")

print("Multiple default parameters:")
create_profile("Alice")  # All defaults
create_profile("Bob", 25)  # Age specified
create_profile("Charlie", 30, "USA")  # All specified
print()






