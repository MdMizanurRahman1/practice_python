#1 Write a program that asks a fisher the length of a zander in centimeters.
# If the zander does not fulfill the size limit,
# the program instructs to release the fish back into the lake
# and notifies the user of how many centimeters below the size limit the caught fish was.
# A zander must be 42 centimeters or longer to meet the size limit.

zander_length=float(input("Enter the length of a zander in centimeters:"))


if zander_length<42:
    difference=42-zander_length
    print("To release the fish back into the lake")
    print(f"{difference} centimeters below the size limit the caught fish was")
else:
    print("The size of the fish is okay")



#2 Write a program that asks the user to enter the cabin class of a cruise ship
# and then prints out a written description according to the list below.
# You must use an if/elif/else structure in your solution.

#LUX: upper-deck cabin with a balcony.
# A: above the car deck, equipped with a window.
# B: windowless cabin above the car deck.
# C: windowless cabin below the car deck.
# If the user enters an invalid cabin class, the program outputs an error message Invalid cabin class.

user=input("Enter the cabin class of a cruise ship:")

if user == "LUX":
    print("upper-deck cabin with a balcony.")
elif user == "A":
    print("above the car deck, equipped with a window.")
elif user == "B":
    print("windowless cabin above the car deck.")
elif user == "C":
    print("windowless cabin below the car deck.")
else:
    print("Invalid cabin class")



#3 Write a program that asks for the biological gender and hemoglobin value (g/l).
# The program the notifies the user if the hemoglobin value is low, normal or high.

# A normal hemoglobin value for adult females is between 117-155 g/l.
# A normal hemoglobin value for adult males is between 134-167 g/l.


user_gender=input("Enter your gender:")
h_value=int(input("Enter your hemoglobin value (g/l):"))

if user_gender=="female":
   if h_value>=156:
       print("high")
   elif h_value<=116:
       print("low")
   else:
       print("normal")

elif user_gender=="male":
    if h_value >= 168:
        print("high")
    elif h_value <= 133:
        print("low")
    else:
        print("normal")


#4 Write a program that asks the user to enter a year and notifies the user whether the input year is a leap year.
# A year is a leap year if it is divisible by four.
# However, years divisible by 100 are leap years only if they are also divisible by 400.

user_year=int(input("Enter a year:"))

if user_year % 400 ==0:
    print(f"{user_year} is a leap year")
elif user_year%4==0 and user_year%100!=0:
    print(f"{user_year} is also a leap year")
else:
    print(f"{user_year} is not a leap year")









