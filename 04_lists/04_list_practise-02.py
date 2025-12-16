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
