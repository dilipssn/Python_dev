
# file --> course_info.txt
# file = open("example.txt", "r")
# file.read()
# file.close()


# read()
# with open("course_info.txt", "r") as file:
#     content = file.read()  # entire file as string
#     print(content)
# # file automatically closed here

# # readlines()
# with open('course_info.txt') as file:
#     lines = file.readlines()  # Returns a list of lines
#     print(lines)

# # Efficient and in-practise approach
with open('course_info.txt') as file:
    for line in file:
        print(line.strip()) 

# # Efficient and in-practise approach
# with open('dummy.txt') as file:
#     for line in file:
#         print(line.strip()) 

# JSON file

# Incorrect way (String will be fetched)
# with open('person.json') as file:
#     for line in file:
#         print(line.strip()) 


import json

# json.load -> used to load from file
with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)
    print(type(person))

# find the hobbies of person
print(f"Person's hobbies: {person['hobbies']}")


# loads -> used to load from string
# json_string = "{'name': 'Bob', 'age': 25}"  # json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes:
json_string = '{"name": "Bob", "age": 25}'  # Correct JSON format
python_dict = json.loads(json_string)  # dict
print(python_dict)


# load/loads -> json file/string to python dict

# dump/dumps -> python dict to json file/string


# Json with list of dicts
with open('persons.json', 'r') as file:
    persons = json.load(file)   # list of dicts
    print(f"Parsed: persons.json")
    print(persons)
    print(type(persons))

# The key differences to remember:
# json.load() - reads from a file
# json.loads() - reads from a string
# json.dump() - writes to a file
# json.dumps() - converts to a string

# CSV file
import csv

# #not recommended
# with open('employees.csv', 'r') as file:
#     csv_reader = csv.reader(file)
#     for row in csv_reader:
#         print(row)  # Each row is a list
        
# recommended - parses as dict values
with open('employees.csv', 'r') as file:
    csv_reader = csv.DictReader(file, delimiter='-')
    for row in csv_reader:
        print(row)
