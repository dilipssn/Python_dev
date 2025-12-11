# # concatenation
#
# first = "Hello"
# second = "World"
#
# result = first + " " + second  + " extra chars"
#
# f_str = f"text ... {first} {second}"
#
# print(f_str)
#


# print('-' * 40)
# print('Welcome to programming in python')
# print('-' * 40)
#
#
# # cv = "Dilip\nAWS, DevOps\nChennai"
# cv = """Dilip
# AWS, DevOps
# Chennai
# """
#
# print(cv)

# 0123456   -->
# Python
#  -3-2-1

word = "Python"
print(word[2])
print(word[-2])
print(word[0:3])    # slicing - inclusive of 3, exclusive of 3
print(word[2:])     # 'thon' (from index 2 to end)
print(word[::-1])   # how to reverse a string
print(word[:])  # full string
# print(word[start:end:step])  # full string

text = "  Hello, Python!  "
#       0123456789

# Changing case
text.upper()           # "  HELLO, PYTHON!  "
text.lower()           # "  hello, python!  "
print(text.title())           # "  Hello, Python!  "


# Removing whitespace
print(f"*{text.strip()}*")
print(f"*{text.lstrip()}*")
print(f"*{text.rstrip()}*")


# Find index
print(f"Position of t is: {text.find('t')}")
print(f"Position of Python is: {text.find('Python')}")
print(f"Position of Python is: {text.find('c++')}") # -1

# if word is found, run the script


if text.find("Python") == -1:
    print(f"Not a valid python script")
else:
    print(f"Valid python script. Executing...")

language = 'c++'

if text.find(language) == -1:
    print(f"Not a valid {language} code")
else:
    print(f"Valid {language} code. Executing...")


filenames = ["test_logs.json", "test_logs.csv", "test_logs.log"]

for filename in filenames:
    if filename.endswith(".json"):
        print(f"{filename} Parsing json files")
        ...
    else:
        print(f'{filename} : Not a json format')


# Replace string'   # replace all occurrences
text = "Hello, Python. Hello"
replace_str = text.replace("Hello", "Hi")  # "  Hi, Python!  "
print(replace_str)
















