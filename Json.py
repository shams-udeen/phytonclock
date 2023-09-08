import json 

person = '{name:"emmanuel", age:40}'

# convert from json to python 
convert = json.loads(person)

# the result is a python dictionary 
print(convert['age'])


# CONVERTING PYTHON TO JSON 

# a Python object (dict):
person = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert Python into JSON:
convert = json.dumps(x)

# the result is a JSON string:
print(convert)
