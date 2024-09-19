
# keywords
# import keyword
# print(keyword.kwlist)


# logical operators
# print(not(10 < 5
#     and 1 > 3
#     or "a" == "c"))


# assignment operators
# brand = "amigoscode"
# brand = "Nike"
# print(brand)


# number = 20986


# if statements
# if number > 2 and number <10:
#     print()
#     print(f"Yes, {number} is greater than 2.")
# elif number >= 10:
#     print()
#     print(f"Did you learn how to count digits in elementary school or were you too busy smearing your own excrement on the walls? "
#           f"Yes, {number} is greater than 2.")
# elif number < 2 and number >= 1:
#     print()
#     print(f"No, {number} is less than 2.")
# elif number < 1:
#     print()
#     print(f"There is not even a digit in front of the decimal point in {number}. Yes, it is less than two.")
# elif number == 2:
#     print()
#     print(f"The fuck kind of question is that?")
# print()
# print("Dumbass.")


# lists - Lists are ordered and duplicates are allowed.
# numbers = [1, 1, 2, 3, 4, -1, 0]
# numbers.sort()
# numbers.append(10)
# print(len(numbers))
# numbers.clear()
# print(5 not in numbers)
# numbers.remove(numbers[3])
# numbers.pop()
# del numbers[1:7]
# print(numbers)


# sets - Sets are orderless and duplicates are not allowed.
# numbersList = [1, 1, 2, 3, 5]
# numbersSet = {1, 1, 2, 3, 5}
# lettersSet = {"A", "A", "B", "C", "C"}
# lettersSet.remove("B")
# print(numbersList)
# print(numbersSet)
# print(lettersSet)

# set unions and intersections
# numbersA = {1, 2, 3}
# numbersB = {3, 4, 5}
# union = numbersA | numbersB
# intersection = numbersA & numbersB
# difference1 = numbersA - numbersB
# difference2 = numbersB - numbersA
# print(f"Union = {union}")
# print(f"Intersection = {intersection}")
# print(difference1)
# print(difference2)


# dictionaries
# person = {
#      "name": "Jamal",
#      "age": 20,
#      "address": "USA"
# }
# person["age"] = 21
# print(person["name"])
# print(person["age"])
# print(person.get("age")) # Better alternative
# print(person["address"])
# print(person.keys())
# print(person.values())


# for loops
# names = {"Ahmed", "Anna", "James", "Camille"}
# for name in names:
#     print(name)


# person = {
#     "name": "Jamal",
#     "age": 20,
#     "address": "USA"
# }
# print(person.items())
# for key, value in person.items():
#     print(f"key:{key} value:{value}")
# for key in person:
#     print(f"key:{key} value:{person[key]}") # Better alternative


# exercise (killed it)
# numbers = [1, 3, 5, 6, 7, 9]
# sum = 0
# for number in numbers:
#     sum += number
# print(f"The sum is {sum}")


# while loops
# number = 0
# while number < 10:
#     number += 1
#     print(number)
# else:
#     print("while loop ended")

# while number < 10:
#     if number == 5:
#         print("number is 5 hooray")
#     number += 1

# break and continue
# while number < 10:
#     number += 1
#     if number < 5:
#         continue
#     print(number)

# while number < 10:
#     number += 1
#     if number == 5:
#         break
#     print(number)

# for n in [1, 2, 3, 4, 5, 6, 7]:
#     if n == 5:
#         break
#     print(n)


# functions
# def greet():
#     print("Hello, how are you?")
# greet()

# def greet(name, age):
#     if age % 10 == 1 and age != 11:
#         print(f"Hello {name}, how was your {age}st Birthday?")
#     elif age % 10 == 2 and age !=12:
#         print(f"Hello {name}, how was your {age}nd Birthday?")
#     else:
#         print(f"Hello {name}, how was your {age}th Birthday?")
# greet("Jamila", 21)
# greet("Alex", 11)

# def greet(name, age=-21):
#     print(f"Hello, {name}")
#     if age < 0:
#         age *= -1
#     print(f"I know your age = {age}")

# def greet(name, age=-21):
#     print(f"Hello, {name}")
#     if age >= 0:
#         print(f"I know your age = {age}")
# greet("Biden")
# greet("Trump", 78)

# def is_adult(age):
#     if age >= 16:
#         print("adult :)")
#     else:
#         print(f"{age} is not yet an adult :(")

# def is_adult(age):
#     if age >= 16:
#         return True
#     else:
#         return False
# result = is_adult(10)
# print(result)

# def is_adult(age):
#     return age >= 16 # Better alternative
# result = is_adult(10)
# print(result)

# def convertGender(gender="unknown"):
#     if gender.upper() == "M":
#         return "Male"
#     elif gender.upper() == "F":
#         return "Female"
#     else:
#         return gender
# print(convertGender("F"))
# print(convertGender("NB"))


# built-in functions
# import math
# pi = math.pi
# def sin(x):
#     return math.sin(x)
# print(sin(0))


# creating modules
# from calculator import divide
# from calculator import multiply
# from calculator import add
# from calculator import subtract
# from calculator import power
# print(divide(2, 2))
# print(power(2, 4))
# print(subtract(2, 4))
# print(add(2, 4))
# print(multiply(2, 4))


# creating classes and objects
# class Phone:
#
#     # def __init__(self):
#     #     super().__init__() - DID NOT EXPLAIN
#
#     # def __init__(self, brand, price):
#     #     self.brand = brand
#     #     self.price = f"${price}"
#
#     def call(self, phone_number):
#         print(f"{self.brand} is calling {phone_number}")
#
#     def __str__(self) -> str:
#         return f"Brand {self.brand} Price {self.price}"
#
#
# iphone = Phone("iPhone 13", 599.99)
# samsung = Phone("Samsung S20", 899.99)
#
# print(iphone.brand)
# print(iphone.price)
#
# print(iphone)
# print(samsung)


# working with dates
# from datetime import datetime
# from datetime import date
#
# # print(datetime.now())
# # print(date.today())
# # print(datetime.now().time())
# # print(datetime.now().day)
#
# now = datetime.now()
# print(now)
#
# print(now.strftime("%m/%d/%Y %H:%M:%S"))
# print(now.strftime("%B %d, %Y %H:%M:%S"))
# print(now.strftime("%b %d, %Y %H:%M:%S"))
#
# print(date.today().strftime("%m/%d/%Y"))


# creating files
# w writing, a appending, r reading, r+ reading/writing
# file = open("./data.csv", "r")
# file.write("id, name, email\n")
# file.write("1, Noah, noahsummerlin5@gmail.com\n")
# file.write("2, Kat, kat.bullough@gmail.com\n")
# file.write("3, Wang, wangfire@gmail.com\n")
# print(file.read())
#
# for line in file:
#     print(line)
#
# # file.close()
#
# import os.path
# filename = "./data.csv"
# if os.path.isfile(filename) is True:
#     with open(filename, "r") as file:
#         print(file.read())
# else:
#     print(f"file {filename} does not exist")


# fetching data from internet
# from urllib import request
# r = request.urlopen("http://www.google.com")
# # print(r)
# print(r.getcode())
# print(r.read())
#
# from urllib import request
# import json
#
# url = "https://official-joke-api.appspot.com/random_ten"
# r = request.urlopen(url)
# print(r.getcode())
# data = r.read()
# jsonData = json.loads(data)
# print(jsonData)
#
# class Joke:
#
#     def __init__(self, setup, punchline):
#         self.setup = setup
#         self.punchline = punchline
#
#     def __str__(self):
#         return f"setup {self.setup} punchline {self.punchline}"
#
#
# jokes = []
#
# for j in jsonData:
#     setup = j["setup"]
#     punchline = j["punchline"]
#     joke = Joke(setup, punchline)
#     jokes.append(joke)
#
# print(f"Got {len(jokes)} jokes")
#
# for joke in jokes:
#     print(joke)
#
#
# # pip and modules
# import json
# import requests
# url = "https://official-joke-api.appspot.com/random_ten"
# response = requests.get(url)
# print(response.status_code)
# data = response.text
# jsonData = json.loads(data)
# print(jsonData)
#
# class Joke:
#
#     def __init__(self, setup, punchline):
#         self.setup = setup
#         self.punchline = punchline
#
#     def __str__(self):
#         return f"Setup: {self.setup}\nPunchline: {self.punchline}"
#
#
# jokes = []
#
# for j in jsonData:
#     setup = j["setup"]
#     punchline = j["punchline"]
#     joke = Joke(setup, punchline)
#     jokes.append(joke)
#
# print(f"Got {len(jokes)} jokes")
#
# for joke in jokes:
#     print(joke)


# numbers = [1, 3, 5, 6, 7, 9]
# sum = 0
# for value in numbers:
#     sum += value
# print(sum)


# # gravity proof of concept
# import math
#
# t = 0
#
# # x-variables
# xa = 0
# xv = 0
# xp = 0
#
# # y-variables
# ya = 0
# yv = 0
# yp = 0
#
# # z-variables
# # za = 0
# # zv = 0
# # zp = 0
#
# distance = math.sqrt((20-xp)**2+(20-yp)**2)
#
# while t<=100:
#
#     if xp<20: xa = (10 / ((20 - xp) ** 2)) #x-gravity and integrations
#     if xp>20: xa = (-10 / ((20 - xp) ** 2))
#     else: xa = 0
#     xv += 0.01*xa
#     xp += 0.01*xv
#
#     if yp<20: a = (10 / ((20 - p) ** 2)) #y-gravity and integrations
#     if yp>20: a = (-10 / ((20 - p) ** 2))
#     else: a = 0
#     v += 0.01*a
#     p += 0.01*v
#
#     print(f"Time = {t} seconds, Position = {p} meters")
#
#     t += 0.01


# # classes and objects: __init__, __iter__, and __next__
# class MyNumbers:
#     def __init__(self, x):
#         self.x = x
#
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x
#
#
# myclass = MyNumbers(5)
# myiter = iter(myclass)
#
# print(myclass.x)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))


# # use json to convert Python to JS and vice versa
# import json
#
# thisDict = {
#     "name": "BigBallsMcGee",
#     "balls": "large",
#     "ballsizes": ["large", "larger", "largest"],
#     "ballsizes2": ("large", "larger", "largest")
# }
#
# thisObject = json.dumps(thisDict)
# print(thisObject)
#
# thisDictAgain = json.loads(thisObject)
# print(thisDictAgain.items())


# # use regular expressions
# import re
#
# txt = "The rains down in Spain"
# x = re.search("^The.*Spain$", txt)
#
# if x:
#     print("YES! We have a match!")
# else:
#     print("No match, alas")


# # try, except, finally
# #The try block will generate an error, because x is not defined:
# try:
#     print(x)
# except:
#     print("An exception occurred")
# else:
#     print("Nothing went wrong")
# finally:
#     print("The code was tested")


# # raising exceptions
# x = -1
#
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")


# # deleting files
# import os
#
# f = open("demofile.txt", "w")
# f.write("this is a sample file")
# f.close()
#
# f = open("demofile.txt", "rt")
# for line in f:
#     print(line)
# f.close()
#
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")
#
# # deleting **empty** folders
# os.rmdir("myfolder")

# numpy
import numpy as np
# arr = np.array([1, 3, 5, 7])
# print(arr[0] + arr[3])

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)