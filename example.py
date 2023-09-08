import module

print(module.greeting('emmanuel'))

x = module.person1['name']
y = module.person1['age']
print(y)

# RENAMING A MODULE IN PYTHON 
import module as balablue 

print(balablue.greeting('Bizmarrow'))


import platform

x = platform.system()
print(x)




x = dir(platform)
print(x)


# import only a specific item in a file 
from module import person1

print (person1["age"])


