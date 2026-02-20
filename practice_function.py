#1 Write a function that returns a random dice roll between 1 and 6.
# The function should not have any parameters.
# Write a main program that rolls the dice until the result is 6.
# The main program should print out the result of each roll.

import random

def dice_roll():
    dice1 = random.randint(1, 6)
    return dice1

dice = 0

while dice!=6:
    dice = dice_roll()
    print(dice)



#2 Modify the function above so that it gets the number of sides on the dice as a parameter.
# With the modified function you can for example roll a 21-sided role-playing dice.
# The difference to the last exercise is that the dice rolling in the main program continues until
# the program gets the maximum number on the dice, which is asked from the user at the beginning.




def dice_roll(sides):
    return random.randint(1, sides)

sides = int(input("Enter the number of sides on the dice: "))

dice = 0

while dice != sides:
    dice = dice_roll(sides)
    print(dice)



#3 Write a function that gets the quantity of gasoline in American gallons
# and returns the number converted to litres.
# Write a main program that asks for a volume in gallons from the user and converts the value to liters.
# The conversion must be done by using the function. Conversions continue until the user inputs a negative value.

# 1 gallon =3.79 liter

user=float(input("enter the quantity of gasoline in gallons: "))



def american_gallons(user):
    converts=user*3.79
    return converts


while user>0:
    gallon=american_gallons(user)
    print(f"{gallon:.2f} litters")
    user=float(input("enter the quantity of gasoline in gallons: "))
#


#4 Write a function that gets a list of integers as a parameter.
# The function returns the sum of all the numbers in the list.
# For testing, write a main program where you create a list, call the function,
# and print out the value it returned.

#a
list_integers=[2, 3, 6, 7, 15,9]

def new_integers(list_integers):
    result=sum(list_integers)
    return result

print(new_integers(list_integers))

#b
def new_list(list_integers):
    total = 0
    for i in list_integers:
        total+=i
    return total
print(new_list(list_integers))


#5 Write a function that gets a list of integers as a parameter.
# The function returns a second list that is otherwise the same as the original list
# except that all uneven numbers have been removed.
# For testing, write a main program where you create a list, call the function,
# and then print out both the original as well as the cut-down list.


old_integers=[3,4,5,6,7,8,9,11,23,33,45,60,34,56,71]

def remove_integers(old_integers):
    new_intergers=[]
    for i in old_integers:
        if i%2==0:
            new_intergers.append(i)
    return new_intergers

result = remove_integers(old_integers)

print(old_integers)
print(result)


#6 Write a function that receives two parameters: the diameter of
# a round pizza in centimeters and the price of the pizza in euros.
# The function calculates and returns the unit price of the pizza per square meter.
# The main program asks the user to enter the diameter and price of two pizzas
# and tells the user which pizza provides better value for money (which of them has a lower unit price).
# You must use the function you wrote for calculating the unit prices.

import math

pizza1=int(input("enter the pizza1 diameter in cm: "))
pizaa1_price=int(input("enter the pizza1 price in euros: "))

pizza2=int(input("enter the pizza2 diameter in cm: "))
pizza2_price=int(input("enter the pizza2 price in euros: "))


def pizza_values(diameter, prize):
    radius=diameter/2
    area=math.pi*radius**2
    meter=area/10000
    result=prize/meter
    return result

pizza_A=pizza_values(pizza1,pizaa1_price)
Pizza_B=pizza_values(pizza2,pizza2_price)

if pizza_A<Pizza_B:
    print(f"pizza1 {pizza_A:.2f} euro price is less than pizza2 {Pizza_B:.2f} euro")
elif Pizza_B<pizza_A:
    print(f"pizza2 {Pizza_B:.2f} euro price is less than pizza1 {pizza_A:.2f} euro")








