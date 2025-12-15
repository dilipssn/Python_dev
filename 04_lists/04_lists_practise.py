# Note: # https://claude.ai/share/66227fa5-4cd7-47ec-a5fa-b0d0e2b15f2e

# List of product names
products = ["iPhone 15", "Samsung Galaxy", "iPad Pro", "MacBook Air", "iPhone 14"]

# Tasks:
# 1. Find all products with "iPhone" in the name
def find_by_name(product: list):
    apple_prod = [] # apple_products is not the right name here. iphone_gadgets, iphone_names etc. are the right names.
    for apple in product: # review comment: its meaningful to keep names apple_products. _prod doesn't give clear meaning, someone may think prod to be production.
        if 'iPhone' in apple: # review comment: it is better to give one line space above for statemet. this makes code readable.
            apple_prod.append(apple)    # review comment: looks good. but in the future, for the one line simple operations to build a list, we need to replace list.append with list comprehensions to improve the performance
    return apple_prod

# print (find_by_name(products))
# ['iPhone 15', 'iPhone 14']

# 2. Check if "iPad Pro" is available
def find_by_name(product: list):
    apple_prod = [] # review: the logic is incorrect here. The question asks if its available. Meaning yes or no -> True or False. We do not need to build a list for checking it. Please see the  check_product function below
    for apple in product:
        if 'iPad Pro' in apple:
            apple_prod.append(apple)
    return apple_prod

def check_product(products, search_product):
    for product in products:
        if product.lower() == search_product.lower():
            return True # Here the loop breaks

    # if the True condition is not met, return False at the end after
    # all the iterations are exhausted for the products
    return False

# print (find_by_name(products))
# ['iPad Pro']

# 3. Count total products
def find_by_name(product: list):    # why is that you have did the same function for all the questions. solution is just len(products)
    apple_prod = []                 # we should use functions only when there is more steps to arrive at a solution. len(list) already is a one liner. So function is not required.
    for apple in product:
        apple_prod.append(apple)
    print (f'total products in the cart are : {len(apple_prod)}')
    return apple_prod
# total products in the cart are : 5
# ['iPhone 15', 'Samsung Galaxy', 'iPad Pro', 'MacBook Air', 'iPhone 14']

# 4. Show products in alphabetical order
def find_by_name(product: list):    # Again, function is not required here. list.sort(reverse=False) will give a one liner solution
    apple_prod = []
    for apple in product:
        apple_prod.append(apple.lower())
                            # review comment: this space is good, likewise need a space in line 42.
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
    print ("Below are the products are out of stock as of now: ")   # this log does not give any info. It just prints this message and returns it. Please log the count.
    return count

print (process_stock(stock))    # Either need to log within the function or outside. Not half half. it will break the continuity of the code.
# Below are the products are out of stock as of now:
# 2

# 2. Find products with low stock (less than 5)
def process_stock(stuffs: list):
    count = 0
    for item in stuffs:
        if item < 5:
            count += 1
    print ("Below are the products are low stock as of now: ")  # Same command as above. Log fully. Give clear information by logging (lesser than 5 )
    return count

stock = [5, 0, 12, 3, 0, 8]
print (process_stock(stock))
# Below are the products are low stock as of now:
# 3

# 3. Calculate total items in warehouse
def process_stock(stuffs: list):    # function names starting with process_ is considered not so useful in programming. process means there could be n number of processing. you should clearly name the function, get_stock_count etc. we dont do any processing here. in general, avoid using process in namings, it is a very begginer level naming convention
    count = len(stuffs)
    print ("Below are the total products stock as of now: ")    # incomplete logging.
    return count

print (process_stock(stock))

# Below are the total products stock as of now:
# 6

# 4. Check if all products are in stock
# incorrect. when the question asks check, the function should return either true or false. please do not name with process_ i think I never gave examples with process in function names. Please follow the notes that we discussed to name.
def process_stock(stuffs: list):    # type hinting of list is correct but naming should be appropriate. stuffs is nowhere related to stocks. we are dealing with stocks not grocery stuffs.
    count = 0                       # refer to my solution below: check_stocks
    for item in stuffs:
        if item == 0:
            count += 1
    print ("Below are the products are out of stock as of now: ")
    return count

def check_stocks(stocks):
    """The function checks if all the stocks are available"""
    # loop through each of the stock
    for stock in stocks:
        # if any stock has 0 value return False
        if stock == 0:
            print(f'Found a stock with 0 items')
            return False

    # otherwise return true
    print(f'All the stocks are available!')
    return True


print (process_stock(stock))
# Below are the products are out of stock as of now:
# 2

# Problem 8: Student Grade Analyzer
# Process student grades:

# Calculate class average
def student_grade_analyzer(students: list): # lets come to this later. Please work on above review comments.
    student_count = 0
    sum_of_score_avg = 0
    for student in students:
        student_count += 1
        std_score = student ["scores"]
        score_avg = (sum(std_score) / len(std_score))
        sum_of_score_avg = sum_of_score_avg + score_avg
    class_avg = (sum_of_score_avg / student_count) // 1
    return f"Class average score is {class_avg}"

print (student_grade_analyzer(students))
# Class average score is 78.0

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


