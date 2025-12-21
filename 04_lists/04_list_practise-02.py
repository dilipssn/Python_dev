# You have a cart with item prices
cart = [29.99, 15.50, 8.99, 45.00]

# Tasks:
# 1. Calculate total price
# 2. Apply 10% discount if total > 50
# 3. Add a new item (price: 12.99)
# 4. Remove the cheapest item
# 5. Count how many items cost more than 20

def shopping_cart():    # try to add docstring. I am adding now.
    """
        The function performs shopping cart operations as follows:
        
        a. Calculates total prices and display
        b. Applies discount for products cost more than 50
        c. Adds an item to the cart
        d. Removes the minimum value cart
        e. Counts the pricey products greater than 20 
    """
    
    cart = [29.99, 15.50, 8.99, 45.00]  
    total_price = sum(cart)
    print (f'Total Price in the cart is :{total_price}')    # Please add a space between two different operations to differentiate
    
    if total_price > 50:
        discounted_cart_price = (total_price - (total_price * 0.1)) // 1
        print (f"discounted_cart_price  :{discounted_cart_price}")

    # add item
    cart.append(12.99)
    print(f"Added a new price Rs. 12.99 into the cart and the new cart is : {cart}")    
    
    # remove item
    cart.remove(min(cart))      # Although single line performs the required operation, it is better to split into two lines as below.
    
    """
    low_cost_product = min(cart)
    cart.remove(low_cost_product)
    """
    print(f"Removed a minimum price from the cart and the new cart is : {cart}")
    
    # <line break>
    count = 0
    for price in cart:
        if price > 20:
            count += 1

    print(f"There are {count} items cost more than Rs. 20 in the cart")

shopping_cart()

# outputs are as below:
# -------------------------
# Total Price in the cart is :99.48
# discounted_cart_price  :89.0
# Added a new price Rs. 12.99 into the cart and the new cart is : [29.99, 15.5, 8.99, 45.0, 12.99]
# Removed a minimum price from the cart and the new cart is : [29.99, 15.5, 45.0, 12.99]
# There are 2 items cost more than Rs. 20 in the cart


# List of product names
products = ["iPhone 15", "Samsung Galaxy", "iPad Pro", "MacBook Air", "iPhone 14"]

# Tasks:
# 1. Find all products with "iPhone" in the name
# 2. Check if "iPad Pro" is available
# 3. Count total products
# 4. Show products in alphabetical order



# List of product names
products = ["iPhone 15", "Samsung Galaxy", "iPad Pro", "MacBook Air", "iPhone 14"]

def find_phone_by_name(cart: list):
    iphone_gadgets = []
    # loop the products list to search for iPhone
    for phone in cart:
         
    # search for iPhone from the item
        if 'iPhone' in phone:
            iphone_gadgets.append(phone)

    # Return the found iPhone  
    return iphone_gadgets

print (find_phone_by_name(gadgets)) # good to segregate into 2 lines.

# Output
# ['iPhone 15', 'iPhone 14']

# 2. Check if "iPad Pro" is available

def check_product(products, search_product):        # Looks good. This is how method signature should be
    for product in products:
        if product.lower() == search_product.lower():
            return True # Here the loop breaks

    # if the True condition is not met, return False at the end after
    # all the iterations are exhausted for the products
    return False

print (search_product(gadgets, 'iPod Pro'))         # use f strings: print(f"{search_product(gadgets, 'iPod Pro') = }")
# True

# 3. Count total products
print(f"The total products in the cart :{len(gadgets)}")    # Simple and good 
 
# The total products in the cart :5

# 4. Show products in alphabetical order
def sort_gadgets_alphabetic (gadgets):  # review: As I said this function is not required. 
    gadgets_lower = []                  # print(list.sort()) will yield the desired result: 
                                        # Sorting doesnt require lower case conversion. 
                                        # Only string comparison requires lower case conversion
    # loop the gadgets to get each gadget in string, lower() is a string func
    for gadget in gadgets:
        gadgets_lower.append(gadget.lower())

    # sorting the list with Aphabetical order (abc ..z) low to high, hence "reverse = False"  
    gadgets_lower.sort(reverse = False)
    return gadgets_lower          # return the result

print (sort_gadgets_alphabetic(gadgets))

# ['iphone 14', 'iphone 15', 'ipod pro', 'macbook air', 'samsung galaxy']


# Product quantities in stock
stock = [5, 0, 12, 3, 0, 8]

# Tasks:
# 1. Find how many products are out of stock (0 quantity)

def find_zero_stock(stuffs: list):
    count = 0
                        # review: this space makes code cleaner
    for item in stuffs:
                        # review: this space is not required. 
        if item == 0:
            count += 1

    print (count, 'products are out of stocks now') # use f strings as like below for meaningful information
    print(f"There are '{count}' products out of stock. Please order new stocks.")

find_zero_stock(stock)

# (2, 'products are out of stocks now')

# 2. Find products with low stock (less than 5)
def find_low_stock(stuffs: list):
    count = 0               # space required
    for item in stuffs:
                            # space not required
        if item < 5:
            count += 1

    print (f"There are {count} products are at low stock range now")

stock = [5, 0, 12, 3, 0, 8] 
find_low_stock(stock)           # this is good. defining array above and invoking below. We can use any no. of stocks to test this way

# There are 3 products are at low stock range now

# 3. Calculate total items in warehouse
print (f"total items in the warehouse are : {len(stock)}")

# total items in the warehouse are : 6

# 4. Check if all products are in stock
def check_stocks(stocks):                                       # Looks good. Need to add argument info and return statement as below when a function accepts arg. We will use this in future sessions.
    """
        The function checks if all the stocks are available
        
        @param  stocks      List of stocks to be validated
        
        @return     True    If all stocks are available
                    False   If any stock is empty   
    """
    # loop through each of the stock
    for stock in stocks:
        # if any stock has 0 value return False
        if stock == 0:
            print(f'Found a stock with 0 items')
            return False

    # otherwise return true
    print(f'All the stocks are available!')
    return True

check_stocks(stock)

# Found a stock with 0 items
# False

📝 Task & Todo Management
Problem 4: Simple Todo List
python
# Your daily tasks
    tasks = ["Buy groceries", "Call mom", "Finish homework", "Go to gym"]

# Tasks:
# 1. Add a new task: "Read a book"

    tasks.append("Go to office")
    print (f"At the tasks list, there a new task added. and the new tasks list is: \n {tasks}")

>>> At the tasks list, there a new task added. and the new tasks list is:
>>> ['Buy groceries', 'Call mom', 'Finish homework', 'Go to gym', 'Go to office']

# 2. Remove "Call mom" (completed!)

    tasks.remove("Call mom")
    print (f"\n From the tasks list, removed a task 'Call mom'as it's completed. New tasks list :\n {tasks}")

>>> From the tasks list, removed a task 'Call mom'as it's completed. New tasks list :
>>> ['Buy groceries', 'Finish homework', 'Go to gym', 'Go to office']
    
# 3. Check if "Go to gym" is in your list

def check_my_task(tasks: list):
    
    # Check if "Go to gym" is in your list
    for task in tasks:                # loop the tasks list and get each task
        if task == "Go to gym":       # checking the match string
            return "Go to gym task found in tasks list"    # return "if" searching task found, if not keep check the next string
    return "Go to gym task not found in tasks list"        # return the for loop, if no match found

>>> check_my_task(["Buy groceries", "Call mom", "Finish homework", "Go to gym"])
'Go to gym task found in tasks list'

# 4. Show how many tasks are pending

    print (f"\n Now there are {len(tasks)} tasks are pending fromt the tasks list")

>>> Now there are 4 tasks are pending fromt the tasks list

# 5. Display tasks in reverse order

    tasks_rev = list(reversed(tasks))
    tasks.reverse()
    print (f"\n Printing the tasks list in reverse order {tasks_rev} \n") 
    print (f"\n Printing the tasks list in reverse order {tasks} \n")
    print (f"\n Printing the tasks list in reverse order {tasks[::-1]}")   # Reverse using slicing concept

>>> Printing the tasks list in reverse order ['Go to office', 'Go to gym', 'Finish homework', 'Buy groceries']
>>> Printing the tasks list in reverse order ['Go to office', 'Go to gym', 'Finish homework', 'Buy groceries']
>>> Printing the tasks list in reverse order ['Go to office', 'Go to gym', 'Finish homework', 'Buy groceries']

>>>

Problem 5: Priority Tasks
python
# Tasks with priority (1=high, 2=medium, 3=low)
priorities = [2, 1, 3, 1, 2]

# Tasks:
# 1. Count how many high priority tasks (priority = 1)
# 2. Find the highest priority value
# 3. Check if there are any low priority tasks

def count_high_priority(priorities: list):
    """ 
    1. Count how many high priority tasks (priority = 1)
    Tasks with priority (1=high, 2=medium, 3=low)
    """ 
    high_priority_count = 0
    for p in priorities:
        if 1 == p:
            high_priority_count += 1
    return f"High priority tasks are :{high_priority_count}"
   
   
>>> count_high_priority(priorities)
'High priority tasks are :2'

def find_high_priority(priorities: list):
    """ 
    Find the highest priority value
    Tasks with priority (1=high, 2=medium, 3=low)
    """
    if 1 in priorities:
        return "Found the highest priority value in priorities list"
    

>>> find_high_priority ([2, 1, 3, 1, 2])
'Found the highest priority value in priorities list'
>>>

def find_low_priority(priorities: list):
    '''
    3. Check if there are any low priority tasks
    Tasks with priority (1=high, 2=medium, 3=low)
    '''
    if 3 in priorities:
        return "Found the low priority value in priorities list"
       
>>> find_high_priority ([2, 1, 3, 1, 2])
'Found the highest priority value in priorities list'


🎓 School & Students
Problem 6: Student Scores
python
# Test scores of a student
scores = [85, 92, 78, 90, 88]

# Tasks:
# 1. Calculate average score
>>> scores = [85, 92, 78, 90, 88]
>>> print(f"The average score from the given list of scores is : {(sum(scores) / len(scores))}")
The average score from the given list of scores is : 86.6
>>>

# 2. Find highest and lowest scores
>>> print (f'From the given list of scores, the highest score is "{max(scores)}" and the lowest score is "{min(scores)}"')
From the given list of scores, the highest score is "92" and the lowest score is "78"
>>>

# 3. Check if student passed all tests (score >= 75)
def check_std_score(scores: list):
    """
    This function find the student's score >= 75 
    which is pass score from the given list of scores
    and conclude student is pass or not
    """
    for score in scores:
        if score <= 75:
            return "Stdent Failed in all tests"  
            # any one score found <75 then loop exits and conclude that student is Failed
    return "Stdent PASSED in all tests"
            
>>> scores = [85, 92, 78, 90, 88]
>>> check_std_score(scores)
'Stdent PASSED in all tests'
>>> scores_2 = [9, 90, 99, 0, 89]
>>> check_std_score(scores_2)
'Stdent Failed in all tests'
>>>


# 4. Count how many scores are above 85
def check_score(scores: list):
    """
    The function counts, how score are >85 from the given scores list of student 
    """
    counter = 0
    for score in scores:
        if score > 85:
            counter += 1
    return f"{counter} score(s) is/are greater then 85 from the scores list"
    
>>> check_score(scores)
'3 score(s) is/are greater then 85 from the scores list'
>>>

# 5. Add a new test score: 95

>>> scores.append(95)
>>> print (f"The new scores list is :{scores}")
The new scores list is :[85, 92, 78, 90, 88, 95, 95]
>>>

Problem 7: Class Attendance
python
# Days present in a month (1=present, 0=absent)
attendance = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1]

# Tasks:
# 1. Count total present days
def count_present_days(attendance):
    counter = 0
    for day in attendance:
        if day == 1:
            counter += 1
    return counter
    
>>> attendance = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1]
>>> count_present_days(attendance)
8
>>>

# 2. Count total absent days
def count_absent_days(attendance):
    counter = 0
    for day in attendance:
        if day == 0:
            counter += 1
    return counter
    
>>> count_absent_days(attendance)
2
>>>

# 3. Calculate attendance percentage

>>> attendance_percentage = (count_present_days(attendance)/len(attendance)) * 100
>>> print (f"Attendance percentage for this month is : {attendance_percentage}")
Attendance percentage for this month is : 80.0
>>>

# 4. Check if attendance is >= 75%

>>> if attendance_percentage >= 75:
...     print (True)
...
True
>>

Problem 8: Student Names
python
# Students in a class
students = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Tasks:
# 1. Add a new student "Frank"
students.append("Frank")
# 2. Remove "Bob" (transferred to another class)
students.remove("Bob")
# 3. Check if "Charlie" is in the class
if "Charlie" in students:
    print ("Yes, the student 'Charlie' is there in the class")
# 4. Show students in alphabetical order
def students_alpha_order(students: list):
    new_student_list = []
    for student in students:
        new_student_list.append(student.lower())
    
    new_student_list.sort()
    return new_student_list
    
>>> students_alpha_order(students)
['alice', 'charlie', 'david', 'eve', 'frank']
>>>
    
# 5. Count total students
>>> print (f"The total students are :{len(students)}")
The total students are :5
>>>



💰 Money & Finance
Problem 9: Monthly Expenses
python
# Your daily expenses this week
expenses = [45, 20, 15, 60, 30, 25, 50]

# Tasks:
# 1. Calculate total spent
# 2. Find your highest expense day
# 3. Find days where you spent more than 40
# 4. Calculate average daily expense
# 5. Add today's expense: 35
Problem 10: Salary Tracking
python
# Monthly salaries for the year (in thousands)
salaries = [50, 50, 52, 50, 55, 50, 50, 58, 50, 50, 60, 50]

# Tasks:
# 1. Calculate total yearly income
# 2. Find months with bonuses (salary > 50)
# 3. Calculate average monthly salary
# 4. Find highest salary month


🎮 Games & Fun
Problem 11: Game Scores
python
# Your scores in 5 games
scores = [120, 150, 90, 200, 110]

# Tasks:
# 1. Find your best score
# 2. Find your worst score
# 3. Calculate average score
# 4. Check if you ever scored above 180
# 5. Add a new game score: 175
Problem 12: Dice Rolls
python
# Results of rolling a dice 10 times
rolls = [3, 6, 2, 6, 1, 4, 6, 5, 2, 6]

# Tasks:
# 1. Count how many times you rolled a 6
# 2. Find the most common roll
# 3. Check if you ever rolled a 1
# 4. Calculate sum of all rolls


🍕 Food & Restaurant
Problem 13: Restaurant Orders
python
# Number of pizzas ordered each day this week
orders = [15, 22, 18, 30, 25, 35, 28]

# Tasks:
# 1. Find busiest day (most orders)
# 2. Find slowest day (least orders)
# 3. Calculate total pizzas sold
# 4. Find days with more than 25 orders
# 5. Calculate average daily orders
Problem 14: Menu Prices
python
# Prices of items on menu
menu_prices = [8.99, 12.50, 6.99, 15.00, 9.99]

# Tasks:
# 1. Find cheapest item
# 2. Find most expensive item
# 3. Calculate average price
# 4. Count items under $10
# 5. Increase all prices by $1 (new list)


🌡️ Weather & Temperature
Problem 15: Weekly Temperature
python
# Daily temperatures (°C) for a week
temperatures = [22, 25, 23, 28, 30, 27, 24]

# Tasks:
# 1. Find hottest day
# 2. Find coldest day
# 3. Calculate average temperature
# 4. Count how many days were above 25°C
# 5. Check if any day was below 20°C


📞 Contacts & Communication
Problem 16: Phone Contacts
python
# List of your favorite contacts
contacts = ["Mom", "Dad", "Best Friend", "Boss", "Sister"]

# Tasks:
# 1. Add a new contact "Gym Trainer"
# 2. Remove "Boss" (changed jobs!)
# 3. Check if "Mom" is in favorites
# 4. Count total contacts
# 5. Show contacts in alphabetical order


🚗 Transportation
Problem 17: Fuel Consumption
python
# Liters of fuel used each week
fuel = [40, 35, 42, 38, 45, 40, 37]

# Tasks:
# 1. Calculate total fuel used
# 2. Find week with highest consumption
# 3. Calculate average weekly consumption
# 4. Count weeks where you used more than 40 liters
Problem 18: Daily Commute (minutes)
python
# Time taken to reach office each day
commute_time = [25, 30, 28, 45, 32, 27, 35]

# Tasks:
# 1. Find longest commute
# 2. Find shortest commute
# 3. Calculate average commute time
# 4. Find days when commute was over 30 minutes


📺 Entertainment
Problem 19: Movie Ratings
python
# Your ratings for movies watched (out of 5)
ratings = [4, 5, 3, 4, 5, 2, 4]

# Tasks:
# 1. Count how many 5-star movies
# 2. Find your lowest rated movie
# 3. Calculate average rating
# 4. Check if you watched any bad movies (rating < 3)
Problem 20: Netflix Watch Time
python
# Hours watched each day this week
watch_hours = [2, 3, 1, 4, 2, 5, 3]

# Tasks:
# 1. Calculate total hours watched
# 2. Find day you watched most
# 3. Calculate average daily watch time
# 4. Count days where you watched more than 3 hours
