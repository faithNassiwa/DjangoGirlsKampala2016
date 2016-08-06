#Donations Manager Quiz 1:
print("\n")
print("Quiz 1")
salary = int(input(" What is your monthly salary? "))
donation = 0
if salary > 1000:
    donation = (10/100) * salary
    print(" You can donate " + "" + str(donation) + "this year!")

else:
    print(" You won't be able to donate this year!")

print("\n")

print("Quiz 2")
# Marathon App using loops Quiz 2:
distance_to_cover = 102 # in miles
rate_of_first_walker = 0 # in miles per hour
rate_of_second_walker = 0 # in miles per hour
walking = True

while walking:
    rate_of_first_walker += 2
    rate_of_second_walker += 1

    if(rate_of_first_walker + rate_of_second_walker == 102):
        print("They meet at {} miles from the first walker and {} miles from the second walker ".format(rate_of_first_walker),.format(rate_of_second_walker))
        break

#Assignment 1 using for
print("\n")
print("Assignment1 using for loop")
numbers = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)

for number in numbers:
    if (number % 3 & number % 5) == 0:
        print("Fizz Buzz")


    elif number % 5 == 0:
        print("Buzz")


    elif number % 3  == 0 :
        print("Fizz Buzz")

    else:
        print(number)


#Assignment1 using while
print("\n")
print("Assignment1 using while loop")
number = 0
n = 15
start = True
while start:
    number += 1
    if (number <= n):
        if(number % 3 == 0):
            print("Fizz")

        elif(number % 5 == 0):
            print("Buzz")

        elif(number % 3 & number % 5 ==0):
            print("Fizz Buzz")

        else:
            print(number)



x = 1 + 3 * 2
y = 1 + (3 * 2)
print(x)
print(y)
# Above two statements produce the same result as we consider the order of precedence and its still maintained in the second statement with the brackets.

# Getting area
width = 2.5
height = 4
area = width * height
print(area)
# Area value is being returned


# "Bananas" = 50
# SyntaxError: can't assign to literal
# Because a string can not be assigned a value, not valid identifier definition/ variable


word = "rapunzellaydownyourhair"
z = word[0:8]
print(z)
# Returns Rapunzel, the first 8 letters in the above statement.

# Operations and Operands
number = 80
q = number / 90  # returns a float , why???
r = float(number) / 90  # returns float
s = int(number / 90)  # returns int
print(q)
print(r)
print(s)

# Operator Precedence
a = 5 * (9 - 7) + 6
print(a)

b = 2 ** 1 + 1
print(b)

c = 6 * 6 - 3
print(c)

d = 6 / 7 - 1
print(d)

# Are block comments still supported?

"""
Testing block comments
Testing block comments
"""

# String Formatting
name = "Faith"
greeting = "Hi {}, hope you are well. Have a good day".format(name)
print(greeting)

# Catpuring User Inputs
first_name = input(" What is your first name? ")
last_name = input(" What is your last name? ")
print("Hi", first_name, last_name, "!")

# conditional statements application
cash_at_hand = int(input(" How much do you have in your wallet? "))  # shillings
price_of_gown = int(input(" How much does the Gown cost? "))

if (cash_at_hand == price_of_gown):
    print("You Can afford the Gown, Purchase")

elif(cash_at_hand > price_of_gown):
    balance = (cash_at_hand - price_of_gown)
    print("You Can Purchase the Gown, your balance/change is ", balance)

elif(cash_at_hand < price_of_gown):
    balance = cash_at_hand - price_of_gown
    print("You Can Purchase the Gown on credit, short by", balance)

else:
    print("You have no money, You can't purchase the gown ")




#Repetitive Statements for looping Example
miles_run = 0
running = True

while running:
    if(miles_run <= 10):
        print( " Still running! on mile {}".format(miles_run))
        miles_run += 1
    else:
        running = False
        print(" Whew! I am tired. ")


# Another using for this time
kingdoms = ("Riverlands", "North", "Vale", "Westernlands")
for kingdom in kingdoms:
    print(kingdom)











