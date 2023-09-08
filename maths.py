x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

# The abs() function returns the absolute (positive) value of the specified number
x = abs(-7.25)
print(x)

# The pow(x, y) function returns the value of x to the power of y (xy)
x = pow(4, 3)
print(x)


# The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a number downwards to its nearest integer, and returns the result

#Import math library
import math

#Round a number upward to its nearest integer
x = math.ceil(1.4)

#Round a number downward to its nearest integer
y = math.floor(1.4)

print(x)
print(y)

# The math.sqrt() method for example, returns the square root of a number
import math

x = math.sqrt(64)

print(x)

# The math.pi constant, returns the value of PI
import math

x = math.pi

print(x)


# PYTHON REGEX

import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

# The findall() function returns a list containing all matches.
import re

#Return a list containing every occurrence of "ai":

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# The search() function searches the string for a match, and returns a Match object if there is a match.
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) 

# If no matches are found, the value None is returned

import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)


# The split() function returns a list where the string has been split at each match

import re

#Split the string at every white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)


# The sub() function replaces the matches with the text of your choice
import re

#Replace all white-space characters with the digit "9":

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# The Match object has properties and methods used to retrieve information about the search, and the result:

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match

