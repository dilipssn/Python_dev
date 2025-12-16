# You have a cart with item prices
cart = [29.99, 15.50, 8.99, 45.00]

# Tasks:
# 1. Calculate total price
# 2. Apply 10% discount if total > 50
# 3. Add a new item (price: 12.99)
# 4. Remove the cheapest item
# 5. Count how many items cost more than 20

def shopping_cart():
    cart = [29.99, 15.50, 8.99, 45.00]
    total_price = sum(cart)
    print (f'Total Price in the cart is :{total_price}')
    if total_price > 50:
        discounted_cart_price = (total_price - (total_price * 0.1)) // 1
        print (f"discounted_cart_price  :{discounted_cart_price}")

    cart.append(12.99)
    print(f"Added a new price Rs. 12.99 into the cart and the new cart is : {cart}")
    cart.remove(min(cart))
    print(f"Removed a minimum price from the cart and the new cart is : {cart}")
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

print (find_phone_by_name(gadgets))

# Output
# ['iPhone 15', 'iPhone 14']

# 2. Check if "iPad Pro" is available


def check_product(products, search_product):
    for product in products:
        if product.lower() == search_product.lower():
            return True # Here the loop breaks

    # if the True condition is not met, return False at the end after
    # all the iterations are exhausted for the products
    return False

print (search_product(gadgets, 'iPod Pro'))
# True

# 3. Count total products
print(f"The total products in the cart :{len(gadgets)}")
 
# The total products in the cart :5

# 4. Show products in alphabetical order
def sort_gadgets_alphabetic (gadgets):
    # Empty list to occumalate gadget in lower case
    gadgets_lower = []

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

     for item in stuffs:

         if item == 0:
             count += 1

     print (count, 'products are out of stocks now')

 find_zero_stock(stock)

# (2, 'products are out of stocks now')

# 2. Find products with low stock (less than 5)
def find_low_stock(stuffs: list):
    count = 0
    for item in stuffs:
        
        if item < 5:
            count += 1

    print (f"There are {count} products are at low stock range now")

stock = [5, 0, 12, 3, 0, 8]
find_low_stock(stock)

# There are 3 products are at low stock range now

# 3. Calculate total items in warehouse
print (f"total items in the warehouse are : {len(stock)}")

# total items in the warehouse are : 6

# 4. Check if all products are in stock
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

check_stocks(stock)

# Found a stock with 0 items
# False
