#1
#Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.

#first way like this
number=1
while number<1000:
   number = number + 1
   if number%3==0:
    print(number)

# second way can be like this
number=1
while number<=1000:
    if number%3==0:
        print(number)
    number+=1



#2 Write a program that converts inches to centimeters until the user inputs a negative value.
# Then the program ends.

user=float(input("Enter a number in inches:"))


while user>=0:
    calculate=user*2.54
    print(calculate,"cm")
    user=int(input("Enter a number in inches: "))


#hard took help
#3 Write a program that asks the user to enter numbers until they enter an empty string to quit.
# Finally, the program prints out the smallest and largest number from the numbers it received.

user = input("Enter a number: ")
smallest=None
largest=None
while user != "":
    number = float(user)
    if smallest == None or number < smallest:
        smallest = number
    if largest == None or number > largest:
        largest = number
    user= input("Enter a number: ")

print ("the smallest number is ",smallest)
print("the largest number is ",largest)
#


#4 Write a game where the computer draws a random integer between 1 and 10.
# The user tries to guess the number until they guess the right number.
# After each guess the program prints out a text: Too high, Too low or Correct.
# Notice that the computer must not change the number between guesses.

import random
user_guess=int(input("Enter a random integer between 1 and 10:"))
game=random.randint(1,10)

while user_guess != game:
    if user_guess > game:
        print("Your guess is too high")
    elif user_guess < game:
        print("Your guess is too low")

    user_guess=int(input("Enter a random integer between 1 and 10: "))
print("You guessed correctly")


#5 Write a program that asks the user for a username and password.
# If either or both are incorrect, the program ask the user to enter the username and password again.
# This continues until the login information is correct or wrong credentials have been entered five times.
# If the information is correct, the program prints out Welcome.
# After five failed attempts the program prints out Access denied.
# The correct username is python and password rules.



user_name=user_password=value=0
while True:
    user_name = input("Enter your user name:")
    user_password = input("Enter your user password:")
    if user_name!="python" or user_password!="rules":
        value+=1
        print("wrong")
        if value==5:
            print("Access Denied")
            break
    else:
        print("welcome")
        break
