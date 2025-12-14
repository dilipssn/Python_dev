# Note: # https://claude.ai/share/66227fa5-4cd7-47ec-a5fa-b0d0e2b15f2e

# List of product names
products = ["iPhone 15", "Samsung Galaxy", "iPad Pro", "MacBook Air", "iPhone 14"]

# Tasks:
# 1. Find all products with "iPhone" in the name
def find_by_name(product: list):
    apple_prod = []
    for apple in product:
        if 'iPhone' in apple:
            apple_prod.append(apple)
    return apple_prod

# print (find_by_name(products))
# ['iPhone 15', 'iPhone 14']

# 2. Check if "iPad Pro" is available
def find_by_name(product: list):
    apple_prod = []
    for apple in product:
        if 'iPad Pro' in apple:
            apple_prod.append(apple)
    return apple_prod

# print (find_by_name(products))
# ['iPad Pro']

# 3. Count total products
def find_by_name(product: list):
    apple_prod = []
    for apple in product:
        apple_prod.append(apple)
    print (f'total products in the cart are : {len(apple_prod)}')
    return apple_prod
# total products in the cart are : 5
# ['iPhone 15', 'Samsung Galaxy', 'iPad Pro', 'MacBook Air', 'iPhone 14']

# 4. Show products in alphabetical order
def find_by_name(product: list):
    apple_prod = []
    for apple in product:
        apple_prod.append(apple.lower())

    apple_prod.sort(reverse=False)
    return apple_prod

print (find_by_name(products))
# ['ipad pro', 'iphone 14', 'iphone 15', 'macbook air', 'samsung galaxy']




# Product quantities in stock
stock = [5, 0, 12, 3, 0, 8]

# Tasks:
# 1. Find how many products are out of stock (0 quantity)
def process_stock(stuffs: list):
    count = 0
    for item in stuffs:
        if item == 0:
            count += 1
    print ("Below are the products are out of stock as of now: ")
    return count

print (process_stock(stock))
# Below are the products are out of stock as of now:
# 2

# 2. Find products with low stock (less than 5)
def process_stock(stuffs: list):
    count = 0
    for item in stuffs:
        if item < 5:
            count += 1
    print ("Below are the products are low stock as of now: ")
    return count

stock = [5, 0, 12, 3, 0, 8]
print (process_stock(stock))
# Below are the products are low stock as of now:
# 3

# 3. Calculate total items in warehouse
def process_stock(stuffs: list):
    count = len(stuffs)
    print ("Below are the total products stock as of now: ")
    return count

print (process_stock(stock))

# Below are the total products stock as of now:
# 6

# 4. Check if all products are in stock
def process_stock(stuffs: list):
    count = 0
    for item in stuffs:
        if item == 0:
            count += 1
    print ("Below are the products are out of stock as of now: ")
    return count

print (process_stock(stock))
# Below are the products are out of stock as of now:
# 2

# Problem 8: Student Grade Analyzer
# Process student grades:

# Calculate class average
# Find top 3 students
# Identify students below passing grade (60)
# Calculate grade distribution (A, B, C, D, F counts)
# Generate progress reports
#
# students = [
#     {"name": "Alice", "scores": [85, 90, 78, 92]},
#     {"name": "Bob", "scores": [70, 65, 80, 75]},
#     {"name": "Tina", "scores": [60, 56, 82, 67]},
#     {"name": "Meena", "scores": [85, 85, 89, 99]}
# ]


