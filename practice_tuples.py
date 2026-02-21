#1 Write a program that asks the user for a number of a month
# and then prints out the corresponding season (spring, summer, autumn, winter).
# Save the seasons as strings into a tuple in your program.
# We can define each season to last three months, December being the first month of winter.

user=int(input("enter a number of a month from 1 to 12: "))

tuple1=("winter","spring","summer","autumn")

if user==12 or user==1 or user==2:
    print(tuple1[0])
elif user==3 or user==4 or user==5:
    print(tuple1[1])
elif user==6 or user==7 or user==8:
    print(tuple1[2])
elif user==9 or user==10 or user==11:
    print(tuple1[3])
else:
    print("Enter a valid number from 1 to 12")


#2 Write a program that asks the user to enter names until he/she enters an empty string.
# After each name is read the program either prints out
# New name or Existing name depending on whether the name was entered for the first time.
# Finally, the program lists out the input names one by one, one below another in any order.
# Use the set data structure to store the names.


userName=input("enter your name: ")

namesList=set()

while userName !="":
    if userName not in namesList:
        print("New name")
    else:
        print("Existing name")

    namesList.add(userName)
    print(userName)
    userName = input("enter your name: ")

print(namesList)

for name in namesList:
    print(name)


#3 Write a program for fetching and storing airport data.
# The program asks the user if they want to enter a new airport,
# fetch the information of an existing airport or quit.
# If the user chooses to enter a new airport,
# the program asks the user to enter the ICAO code and name of the airport.
# If the user chooses to fetch airport information instead,
# the program asks for the ICAO code of the airport and prints out the corresponding name.
# If the user chooses to quit, the program execution ends.
# The user can choose a new option as many times they want until they choose to quit.
# (The ICAO code is an identifier that is unique to each airport.
# For example, the ICAO code of Helsinki-Vantaa Airport is EFHK.
# You can easily find the ICAO codes of different airports online.)


data_airport=dict()

while True:
    user_airport=input("Enter a airport type new or fetch or quit: ")

    if user_airport=="new":
        user_ICAO=input("Enter the ICAO code: ")
        user_airport_name=input("Enter the name of the airport: ")
        data_airport[user_ICAO]=user_airport_name
   #print(data_airport)
    elif user_airport=="fetch":
        user_ICAO2 = input("Enter the ICAO code: ")
        if  user_ICAO2 in data_airport:
            print(data_airport[user_ICAO2])
        else:
            print("The ICAO code does not exist")
    elif user_airport=="quit":
        break
