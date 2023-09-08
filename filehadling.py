# f = open("./file.txt")
# txt = f.read()
# print(txt)
# f.close()

# f = open('./file.txt')
# line = f.readline()
# print(type(line))
# print(line)

# f = open('./file.txt')
# lines = f.readlines()
# print(type(lines))
# print(lines)
# f.close()

# f = open('./file.txt')
# lines = f.read().splitlines()
# print(type(lines))
# print(lines)
# f.close()

# with open('./file.txt') as f:
#     lines = f.read().splitlines()
#     print(type(lines))
#     print(lines)

# with open('./file.txt','w') as f:
#     f.write('This text will be written in a newly created file')

# import os
# os.remove('./files/example.txt')

# import json 
# person_json = '''{
#     "name": "Asabeneh",
#     "country": "Finland",
#     "city": "Helsinki",
#     "skills": ["JavaScrip", "React", "Python"]
# }'''
# # let's change JSON to dictionary
# person_dct = json.loads(person_json)
# print(type(person_dct))
# print(person_dct)
# print(person_dct['name'])

# import json
# # python dictionary
# person = {
#     "name": "Asabeneh",
#     "country": "Finland",
#     "city": "Helsinki",
#     "skills": ["JavaScrip", "React", "Python"]
# }
# # let's convert it to  json
# person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
# print(type(person_json))
# print(person_json)

import json 

person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)

