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
    height = num_check("Height: ")
    cost = num_check("Cost: ")

    # calculate fence perimeter and price
    perimeter = 2 * (width + height)
    price = cost * perimeter

    # display output
    print(f"\nPerimeter: {perimeter} units")
    print(f"Price: ${price:.2f}")

    # ask user if they want to keep going
    keep_going = input("\nPress <enter> to do another calculation or any other key to quit.  ")
    print()

print ("\nThank you for using the fence cost calculator! Goodbye!")
