# Text Type:	       str
# Numeric Types:	   int, float, complex
# Sequence Types:	   list, tuple, range
# Mapping Type:	       dict
# Set Types:	       set, frozenset
# Boolean Type:	       bool
# Binary Types:	       bytes, bytearray, memoryview
# None Type:	       NoneType

Matric_number = 5500
print(type(Matric_number)) # Integer

Matric_number = 'Emmanuel'
print(type(Matric_number)) #string value 

Matric_number = 30.5
print(type(Matric_number)) #float number 

Matric_number = 1j 
print(type(Matric_number)) #complex number 

Students_List = ['Micheal', "obinna", 'muhammed']
print(type(Students_List)) #List which you can also call an array

Students_List = ('Micheal', "obinna", 'muhammed')
print(type(Students_List)) #tuple

values = range(6)
print(type(values))

Person = {"name" : "John", "age" : 36} 
print(type(Person)) #dictionary or call it ObJect

set_of_Items = {"apple", "banana", "cherry"}
print(type(set_of_Items)) # set

set_of_Items = frozenset({"apple", "banana", "cherry"})
print(type(set_of_Items)) #frozenset

Raining = False 
print(type(Raining)) #Boolean

Raining = True
print(type(Raining)) #Boolean

Empty = None 
print(type(Empty))


# Using strings as an array 

greet = "Hello world"
print(greet[0])

# Looping inside a string 

for x in greet:
    print(x)

items = 'balablue'
print(len(items))

# checking if free is present in the following text

message = "The wheater is so cold today"
print('cold' in message)

# using if statement to check for an item in a string 

if "cold" in message:
    print("Yes, 'COLD' is present")

Sentence = "The best things in life are free!"
print("expensive" not in Sentence)


# using if statement to check if an item is not in a string 

if "expensive" not in Sentence:
    print("No 'expensive' Not present")

# Assignment restudy this and study Slicing a strings

# PYTHON STRINGS MODIFICATIONS 

statement = "i am a good boy      "
print(statement.upper())

print(statement.upper())

# To remove white space from strings 
print(statement.strip())

statement = '"I love" "python" language very well'
print(statement.replace("python", 'javascript'))


a = "Hello, World!"
print(a.split(",")) 


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
print(len(thisdict))


thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

# To remove an item in an object or dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# The popitem() removes the last inserted item on the dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)


# The del() keyword remnoves the item with a specified key name 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# The del keyword can also be used to remove the entire dictionary 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict

#print(thisdict) #this will result to an error

# The clear method empties the dictionary 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

