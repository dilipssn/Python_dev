# https://chatgpt.com/share/692842d2-11bc-800c-bf09-cbf6f83e1b7f

# """
# Variables, data types, operators
# """
# # variables
# x = 10
# y = 5.5

# print(x, y)

# x = 20
# y = 55

# print(x, y)

# name = "Alice"
# age = 30 #int
# experience = 5.5    # float

# print(name, age, experience)


# # Basic - primitive data types
# # string - str 
# # integer - int
# # float - float
# # boolean - bool


# # Non-primitive data types 
# # list - list - ex. [1, 'a', 3.5, True]   # mutable collection of primitive data types  
# # tuple - tuple - ex. (1, 'a', 3.5, True)   # immutable collection of primitive data types
# # dictionary - dict   # key-value pairs - keys can be either int, str, float
# # set - set  # unique items(no duplicates)

# s = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
# print(s)

# d = {'name': 'Alice', 'age': 30, 'experience': 5.5}
# print(d)


# # operators
# a = 10
# b = 3
# # arithmetic operators
# print(a + b)  # addition
# print(a - b)  # subtraction
# print(a * b)  # multiplication
# print(a / b)  # division - 3.3333333333333335
# print(a // b) # floor division  - 3
# print(a % b)  # modulus - 1
# print(a ** b) # exponentiation - 1000



# Control flow: if, for, while

# if statement

age = 1
if age > 18:
    print("You are an adult.")
elif age > 10 and age <= 18:
    print("You are a teenager.")
else:
    print("You are a child.")
    
# # for loop
# for i in range(5):  # 0, 1, 2, 3, 4
#     print("Iteration:", i)
    

# my_list = ['a', 'b', 'c', 'd']
# for item in my_list:
#     print("Item:", item)

# # while loop
# count = 0
# while count < 5:    # True
#     print("Count:", count)
#     count += 1


# # break and continue
# for i in range(10):
#     if i == 5:
#         break   # exit the loop
#     print("Iteration with break:", i)

# for i in range(10):
#     if i < 5:
#         continue    # skip the rest of the code and go to next iteration
#     print("Rest of the code", i)

"""Chatgpt"""

items = ["pen", "book", "charger", "laptop"]

for item in items:
    if item == "charger":
        print("Found the charger!")
        break
    print(f"Detected item: {item}")

# 2. Stop password attempts after 3 failures
correct_password = "abc123"

for attempt in range(3):
    pwd = input("Enter password: ")
    if pwd == correct_password:
        print("Access granted")
        break
    else:
        print("Wrong password")
else:
    print("Locked out")


# 3. Stop reading file once a keyword is found
with open("sample.txt") as f:
    for line in f:
        if "ERROR" in line:
            print("Error found!")
            break


# 5. Using break in a while loop menu
while True:
    choice = input("Enter q to quit: ")
    if choice == 'q':
        print("Exiting program...")
        break

# print odd using coninue

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# 2. Skip blank lines while reading a file
with open("data.txt") as f:
    for line in f:
        if line.strip() == "":
            continue
        print("Processing:", line.strip())


#   3. Skip invalid user inputs
values = ["24", "a", "56", "?", "12"]

for v in values:
    if not v.isdigit():
        continue
    print("Valid number:", int(v))

# 4. Skip processing for inactive users
users = [
    {"name": "John", "active": True},
    {"name": "Sara", "active": False},
    {"name": "Leo", "active": True}
]

for user in users:
    if not user["active"]:
        continue
    print("Sending email to:", user["name"])

# 5. Skip items that are out of stock
products = [
    {"name": "Laptop", "stock": 5},
    {"name": "Mouse", "stock": 0},
    {"name": "Keyboard", "stock": 3}
]

for p in products:
    if p["stock"] == 0:
        continue
    print("Processing:", p["name"])
    
# First 5 lines in a file
# with open('sample.txt', 'r') as file:
#     count = 0
#     for line in file:
#         count += 1
#         if count < 2:
#             continue
#         print(line.strip())
        
