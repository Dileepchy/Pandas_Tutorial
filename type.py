# str = "i am student"
# print(str.endswith("student"))  # True
# print(str.capitalize())  # I am student
# print(str.replace("student", "teacher"))  # i am teacher
# print(str.find("q "))  # ['i', 'am', 'student']
# print(str.count("t"))  # ['i', 'am', 'student']

# """name = input("Enter your name: ")
# print("Hello, " + name + "!")  # Hello, <name>!
# print("length of your name is: ", len(name))  # length of your name is: <length>

# s = "My salary is $1000"
# print ("Count of $ is ",s.count("$"))  # My salary is 1000 """

# age = int(input("Enter your age: "))
# if age < 18:
#     print("You are a minor.")  # You are a minor.
# elif age >= 18 and age < 60:
#     print("You are an adult.")
# # You are an adult.
# elif age >= 60:
#     print("You are a senior citizen.")
# # You are a senior citizen. 15   
# else:
#     print("Invalid age entered.")
# # Invalid age entered.

# light = input("Enter the traffic light color (red, yellow, green): ").lower()

# if light == "red":
#     print("Stop")  # Stop
# elif light == "yellow":
#     print("Get ready to stop")
# elif light == "green":
#     print("Go")
# else:
#     print("Invalid traffic light color entered.")

# num = int(input("Enter a number: "))
# if num > 0:
#     print("Positive number")  # Positive number
# elif num < 0:
#     print("Negative number")
# else:
#     print("Zero")

# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even number")  # Even number
# elif num % 2 != 0:
#     print("Odd number")
# else:
#     print("Invalid input")

# marks = int(input("Enter your marks: "))
# if marks >= 90:
#     print("Grade: A")  # Grade: A
# elif marks >= 80:
#     print("Grade: B")
# elif marks >= 70:
#     print("Grade: C")
# elif marks >= 60:
#     print("Grade: D")
# elif marks >= 50:
#     print("Grade: E")
# elif marks < 50:
#     print("Grade: F")
# else:
#     print("Invalid marks entered.")

# marks = int(input("Enter your marks: "))
# if marks >= 90:
#     print("Grade: A")  # Grade: A
# elif marks >= 80 and marks < 90:
#     print("Grade: B")
# elif marks >= 70 and marks < 80:
#     print("Grade: C")
# elif marks >= 60 and marks < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")

# age = 95
# if age >= 18:
#     if age >= 80:
#         print("You are a senior citizen and cannot drive.")
#     else:
#         print("You are an adult and can drive.")
# else:   
#     print("You cannot drive.")



    
"""# WAP to find the largest of three numbers entered by the user.    
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    print("Largest number is:", num1)  # Largest number is: <num1>
elif num2 >= num1 and num2 >= num3:
    print("Largest number is:", num2)
elif num3 >= num1 and num3 >= num2:
    print("Largest number is:", num3)
else:
    print("All numbers are equal.") """
    
# # WAP to check if a number is prime or not.
# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             print(num, "is not a prime number.")  # <num> is not a prime number.
#             break
#     else:
#         print(num, "is a prime number.")  # <num> is a prime number.
# else:
#     print(num, "is not a prime number.")

# # WAP to check if a numple is a multiple of 7 or not.
# num = int(input("Enter a number: "))
# if num % 7 == 0:
#     print(num, "is a multiple of 7.")  # <num> is a multiple of 7.
# else:
#     print(num, "is not a multiple of 7.")
    
    
# # Global variables
# """x = "awesome"

# def myfunc():
#     x = "fantastic"      
# myfunc()
# print("Python is " + x)  # Python is fantastic """

# Python Data Types
# x = "awesome"
# print(type(x)) 
# x = 5
# print(type(x))  # <class 'int'>
# x = 5.5
# print(x)
# print(type(x))  # <class 'float'>
# x = 1j
# print(type(x))  # <class 'complex'>         
# x = ["apple", "banana", "cherry"]
# print(type(x))  # <class 'list'>
# print(x)  # ['apple', 'banana', 'cherry']
# x = ("apple", "banana", "cherry")
# print(type(x))  # <class 'tuple'>
# print(x)  # ('apple', 'banana', 'cherry')
# x = range(6)
# print(type(x))  # <class 'range'>
# x = {"name": "John", "age": 30}
# print(x)  # {'name': 'John', 'age': 30}
# print(type(x))  # <class 'dict'>
# x = {"apple", "banana", "cherry"}
# print(type(x))  # <class 'set'>
# x = frozenset({"apple", "banana", "cherry"})
# print(type(x))  # <class 'frozenset'>
# x = True

# x = 3
# y = 2.8
# z = 1j

# a = float(x)
# b= int(y)
# c = complex(x)

# print(a)  # <class 'int'>
# print(b)  # <class 'int'>
# print(c)  # <class 'int'>

# # Random Number Generation
# import random
# print(random.randrange(1, 10))  # Generates a random integer between 1 and 10
# print(random.random())  # Generates a random float between 0.0 and 1.0

# x = int(2.8)
# y= float(2)
# z = complex(2)
# print(x)  # 2
# print(y)  # 2.0
# print(z)  # (2+0j)
# # Type Casting
# x = "Hello"
# y = "3.5"
# z = "5"
# print(type(x))  # <class 'str'>
# print(type(y))  # <class 'str'>

# # Python String
# print("It's alright")
# print("He is called 'Johnny'")
# print('He is called "Johnny"')

# a = """Python is an incredibly popular and beginner-friendly programming language, 
# making it a great choice for anyone looking to learn to code."""
# print(a[1])


# for x in "banana":
#     print(x)  # b, a, n, a, n, a
    
# x= "Hello, World!"    
# print(len(x))

# txt = "The best things in life are free!"
# print("free" in txt)

# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")
# elif "expensive" not in txt:
#   print("No, 'expensive' is present.")

# b = "Hello, World!"
# print(b[2:5])
# print(b[:5])  # Hello
# print(b[2:])  # llo, World!
# print(b[-5:-2])  # orl

# a = "Hello, World!"
# print(a.upper())
# print(a.lower())  # hello, world!
# print(a.strip())  # Removes any whitespace from the beginning and the end
# print(a.replace("H", "J"))  # Jello, World!
# print(a.split(","))  # Splits the string into a list where each word is a list item
# # print(a.split(" "))  # Splits the string into a list where each word is a list item

# string concatenation
# a = "Hello"
# b = "World"
# c = a + b
# print(c)
# c = a +" "+ b
# print(c)

# def myfun(x, y):
#     print("Hello!", x + y)
    
# myfun(4, 8)

# age = 36
# txt = f"My name is John, I am {age}"
# print(txt)

# price = int(input("Enter price:"))
# txt = f"The price is {price} dollars"
# print(txt)

# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)

# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

# a = 200
# b = 500

# if b > a:
#     print("b is greater than a")
# else:
#     print("a is greater than b")

# print(bool("Hello"))
# print(bool(15))
# x = 200
# print(isinstance(x, int))


# x = 5 
# x += 3
# print(x)

# mylist = ["apple", "banana", "cherry"]
# print(type(mylist))

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])
  
# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1
  
# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# # newlist = [x for x in fruits if "a" in x]

# newlist = [x for x in fruits]
# print(newlist)

# newlist = [x for x in range(10) if x < 5]

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)

# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist[:]
# print(mylist)

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1)

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)

# thistuple = ("apple", "banana", "cherry")
# print(thistuple)
# print(type(thistuple))  # <class 'tuple'>

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[:4])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.symmetric_difference(set2)

# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.symmetric_difference_update(set2)

# print(set1)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)


# dict = {  
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
#     }
# x = dict["model"]
# print(x)  # Mustang

# x = dict.keys()
# print(x)  # dict_keys(['brand', 'model', 'year'])

# x = dict.values()
# print(x)  # dict_values(['Ford', 'Mustang', 1964])

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.items()

# print(x) #before the change

# car["color"] = "red"

# print(x) #after the change

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# print(myfamily["child1"]["name"])  

# i = 1
# while i < 6:
#     i += 1
#     if i == 3:
#         continue  # Exit the loop when i is 3
#     print(i)

# for i in range(2, 6):
#   print(i)

# for x in range(2, 30, 6):
#   print(x)

# for x in range(6):
#   if x == 3: break
#   print(x)
# else:
#     print("Finally finished!")

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)

# def my_function(fname, lname):
#     print(fname + " " + lname)
    
# my_function("Ram", "Yadav")  # Hello from a function!

# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")

# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# def my_function(x):
#   return 5 * x

# print(my_function(3))  # 15
# print(my_function(5))  # 25
# print(my_function(9))  # 45

# def rec(k):
#     if k > 0:
#         result = k + rec(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result

# print(" Recursion Example Results")
# print(rec(6))  

# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)
# mytripler = myfunc(3)

# print(mydoubler(11))
# print(mytripler(11))

# Python Classes and Objects
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# #Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")
# x.printname()

# # class Student(Person):
# #   pass
# # x = Student("Mike", "Olsen")
# # x.printname()  # Mike Olsen

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

# x = Student("Mike", "Olsen", 2019)
# print(x)  # 2019

# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))

# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Drive!")

# class Boat:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Sail!")

# class Plane:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang")       #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747")     #Create a Plane object

# for x in (car1, boat1, plane1):
#   x.move()

# def myfunc():
#   x = 300
#   def myinnerfunc():
#     print(x)
#   myinnerfunc()

# myfunc()

# import mymodule as mx

# mx.greetings("Alice")  # Hello, Alice!
# a = mx.person1["name"]
# print(a)  # John
# b = mx.person1["age"]
# print(b)  # 36
