# ask the user for the width and height
# (assume they put in valid data)

width = float(input("Width: "))
height = float(input("Height: "))

#calculate the area / perimeter
area = width * height
perimeter = 2 * (width + height)

# output the area and perimeter3
print(f"\nPerimeter: {perimeter} units")
print(f"Area: {area} units")

