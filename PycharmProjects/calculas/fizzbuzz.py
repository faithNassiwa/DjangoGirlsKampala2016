# Assignment1 while getting upper limit from user
print("\n")
print("Lets play the fizz buzz game.")

# initializing number
number = 0

# Capturing number input from the user and assigning it to a variable n
n = int(input("Please enter a number to be used as the upper limit for the fizz buzz game: "))

# Starting loop
while True:
    number += 1  # Increment the number if it is less than n
    if number <= n:  # Check whether the initialized number is greater than user input number
        if number % 3 == 0:  # Check whether number is divisible by 3 and gives a remainder of 0,
            if number % 5 == 0:  # Check whether number is divisible by 3 and gives a remainder of 0,
                print("Fizz Buzz")
            else:
                print("Fizz")

        elif number % 5 == 0:  # Check whether number is divisible by 5 and gives a remainder of 0
            print("Buzz")

        else:
            print(number)  # if number does not meet any of the above conditions, print the number.