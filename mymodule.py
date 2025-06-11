# def greetings(name):
#     print("Hello, " + name + "!")
    
# person1 = {
#   "name": "John",
#   "age": 36,
#   "country": "Norway"
# }

# x = min(5, 10, 25)
# y = max(5, 10, 25)

# print(x)
# print(y)

# x = abs(-7.25)

# print(x)

# x = pow(4, 3)

# print(x)

# import math

# x = math.sqrt(64)

# print(x)

# x = math.ceil(1.4)
# y = math.floor(1.4)

# print(x) # returns 2
# print(y)

# import math

# x = math.pi

# print(x)

# import json

# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y)

# import json

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# print(json.dumps(x))

# import re

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# print(x)  # returns a match object

# import re
# txt = 'The rain in Spain'
# x = re.search('a', txt)
# print(x.start())

# import re
# txt = 'The rain in Spain'
# x = re.search('\s', txt)
# print(x.start())

# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")
  
# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")
  
# x = "hello"

# if not type(x) is int:
#   raise TypeError("Only integers are allowed")

# txt = f"The price is {95:.2f} dollars"
# print(txt)

# price = 59
# tax = 0.25
# txt = f"The price is {price + (price * tax)} dollars"
# print(txt)

name = input("Enter your name:")
print(f"Hello {name}")