# ask the user for width and
# loop until they enter a number that is greater than zero

def num_check(question):

    error = "Please enter a number that is greater than zero\n"
    while True:

        try:
            # ask the user for a number
            response = float(input(question))

            # check that the number is greater than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# main routine starts here

keep_going = ""
while keep_going == "":

    # get width and height
    width = num_check("Width: ")
    print(width)
    print()
    height = num_check("Height: ")
    print(height)

    # calculate area and perimeter
    area = width * height
    perimeter = 2 * (width + height)

    # display output
    print(f"\nPerimeter: {perimeter} units")
    print(f"Area: {area} units")

    # ask user if they want to keep going
    keep_going = input("\nPress <enter> to continue or any other key to quit.  ")
    print()

print ("\nThank you for using the area / perimeter calculator! Goodbye!")
