# print("Hello World")
# print("What's up?")

# #Datatypes
# #anything between quotes is a string
# print("There is no mistake here.")

# #integers/numbers
# print(7)
# print(7 + 9)
# print(7+9)

# print(4-8) #-4
# print(3*3) #9
# print(25/5) #5
# print(25/6) #4.something
# print(4**2) #16

# print(23%4) #3

# #functions and methods
# name = "John Jacob Jingleheimer Schmidt"
# print(name)

# print("Hello" + str(4))
# print(int("4"))

#Inputs!
# firstName = "Sean"
# lastName = input("What is your last name?\n")
# print("Top o' the mornin' to you, " + firstName + " " + lastName.lower().capitalize() )
# print("Top o' the mornin' to you, " + firstName + " " + lastName.title() )

#Challenge
#Ask for the user's age, then tell them
#1) how old they will be in 3 years.
#2) What year they'd turn 65
#3) If they're old enough to vote






#Control Flow
# number = int(input("What's your favorite number?\n"))
# if number%2 == 0:
#     print("Your number is even!\n")
# else:
#     print("Your number is odd!\n")
    
# Challenge
# Edit the code so that if a user types
# in something like "nine" or 1.2, the
# code will alert the user to try again




#For Loops!
favAnimal = "Ostriches"
print(favAnimal[4])
print("The first letter is " + favAnimal[0])
print("The second letter is " + favAnimal[1])
print("The third letter is " + favAnimal[2])

for i in range(0,len(favAnimal)):
    print("The " + str(i) + "th letter is " + favAnimal[i])