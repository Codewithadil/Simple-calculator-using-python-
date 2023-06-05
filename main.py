import time #it is time module

print ("Hello World")

print (5+10)

print(256*256)

print("---Your poem here---")

# # don't remove this line
# print('Hey I am a good boye \nand viewer is also a good girls')

# print("how are you \"how is your health\"") #escape sequence character

# print("who", 7,4,8, sep="~", end="009") #using seprator attribute to seprate all statement
# print("Adil")

# a = 1   #integer data type
# print(a)

# Adil = 86
# b = Adil

# print(type(b))

# c = "Adil"
# print (c)


# # mathematicals operations
# print(5+6) #addition
# print(15-6) #subtraction
# print(15*6) #multiplication 
# print(15/6) #divison
# print(15//6) #floor division
# print(5%3) #modular 
# print(2**4) #exponantial

# n = 15
# m = 7
# ans1 = n+m
# print("Addition of",n,"and",m,"is", ans1)
# ans2 = n-m
# print("Subtraction of",n,"and",m,"is", ans2)
# ans3 = n*m
# print("Multiplication of",n,"and",m,"is", ans3)
# ans4 = n/m
# print("Division of",n,"and",m,"is", ans4)
# ans5 = n%m
# print("Modulus of",n,"and",m,"is", ans5)
# ans6 = n//m
# print("Floor Division of",n,"and",m,"is", ans6)

# #typecasting is use to conver one data type into anothe data type
# a = "1"
# # a = 1
# b = "2"
# # b = 2
# print(int(a) + int(b))

# # Implicit TypeCasting
# c = 1.9
# d = 8

# print(c + d)

# # input function 
# a = input("Enter your name: ")
# print("My name is", a)

# x = input("Enter first number: ")
# y = input("Enter second number: ")
# # print(x  + y)

# print(int(x) + int(y))

#strings in python

name = "Harry"
friend = "Rohan"
anotherFriend = 'Lovish'
apple = '''He said, 
Hi Harry
hey I am good
"I want to eat an apple'''  # we want to right multi line para you can also use """ """ or ''' ''' or escap charecter like \
 
print("Hello, " + name)
# print(apple) 
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) # Throws an error
print("Lets use a for loop\n")
for character in apple:
    print(character)

# String Slice

fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen)
# print(fruit[0:4]) # including 0 but not 4
# print(fruit[1:4]) # including 1 but not 4
# print(fruit[:5])
# print(fruit[0:-3])
# print(fruit[:len(fruit)-3]) # calculation like 5 - 3 = 2 so output is  Ma
print(fruit[-1:len(fruit) - 3]) # not get any output it's show blank 
print(fruit[-3:-1]) #output : ng

# Quick Quiz:
nm = "Harry"
print(nm[-4:-2])

# string method

# Strings are immutable
a = "!!!Harry!! !!!!!!!!! Harry !!!"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry", "John"))
print(a.split(" "))
blogHeading = "introduction tO jS"
print(blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Harry"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh"))
# print(str1.index("ishh"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "       #using Tab
print(str2.isspace())

str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())

#if else part

vivoPrice = 28000
budget = int(input("Please enter your budget is :  "))

if(budget >= vivoPrice):
    print("You can purchage the Vivo v30 pro phone")
elif(((budget < 27999) and (budget > 25000)) ):
    print("You can purchases vivo v27")
else:
    print("Sorry, Your budget is low")

# time wise day declear using if else ondition

timestamp = time.strftime("%H:%M:%S")
print(timestamp)
if(timestamp > "12:00:00" and timestamp < "13:00:00"):
    print("Good Morning")
elif(timestamp > "13:00:00" and timestamp < "14:00:00"):
    print("Good Afternoon")
else:
    print("Good Evening")


