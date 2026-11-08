# ask the user for width and
# loop until they enter a number that is greater than zero

error = "Please enter a number that is greater than zero\n"
while True:

    try:
        # ask the user for a number
        width = float(input("Width: "))

        # check that the number is greater than zero
        if width > 0:
            break
        else:
            print(error)

    except ValueError:
        print(error)