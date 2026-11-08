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


# main routine goes here
for item in range(0, 2):
    width = num_check("Width: ")
    print (width)

print()

for item in range(0, 2):
    height = num_check("Height: ")
    print (height)