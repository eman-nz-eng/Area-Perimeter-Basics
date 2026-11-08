# ask the user for their name
username = input ("What is your name? ")

# ask the user for their favourite number (integer)
fav_num = int(input("What is your favourite number? "))

# double, halve and square the user's favourite number
double = fav_num * 2
halve = fav_num / 2
square = fav_num ** 2

# greet the user
print(f"\nHi {username}, your favourite number is: {fav_num}")

# output the results of doubling, halving and
# squaring their favourite number
print (f"The double of your favourite number {fav_num} is: {double}, the halve is: {halve}, and the square is: {square}.")

print ("\nHave a nice day!")
