# Example 3: Mathematical function สี่เหลี่ยม
def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area"""
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)


# Example 3: Mathematical function สามเหลี่ยม
def calculate_triangle_area(height, width):
    """Calculates and displays rectangle area"""
    area = 0.5 * height * width 
    print(f"triangle with length {height} and width {width}")
    print(f"Area = 0.5 * {height} × {width} = {area}")
    print()

print("Calculating triangle areas:")
calculate_triangle_area(5, 3)
calculate_triangle_area(10, 7)


# การหาพื้นที่วงกลม
def calculate_circle_area(radius):
    """Calculates and displays circle area"""
    area = 3.14 * radius ** 2 
    print(f"circle with radius {radius}")
    print(f"Area = 3.14 × {radius}² = {area:.2f}")
    print()

print("Calculating circle areas:")
calculate_circle_area(5, 3)
calculate_circle_area(10, 7)



