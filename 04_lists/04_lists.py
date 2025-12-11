def apply_discount(cart):
    # 1. Calculate total price
    total = sum(cart)
    print(f"{total = }")

    # 2. Apply 10% discount if total > 50
    # check if total > 50
    if total > 50:
        # calculate 10%
        discount = total * 0.1
        print(f"{discount = }")

        # subtract from total
        total = (total - discount) // 1

    print(f"{total =}")
    return total


cart_1 = [
    29.99,
    15.50,
    8.99,
    45.00
]

apply_discount(cart_1)

cart_2 = [
    40,
    40
]

apply_discount(cart_2)

# 3. Add a new item (price: 12.99)
cart_2.append(12.99)
apply_discount(cart_2)

# 4. Remove the cheapest item
print(cart_1)
cheapest = min(cart_1)
print(f"{cheapest = }")
cart_1.remove(cheapest)
print(cart_1)
apply_discount(cart_1)



# 5. Count how many items cost more than 20
counter = 0

# traverse each item
for item in cart_1:
    print(f"{item = }")

    # check greater than 20
    if item > 20:
        print(f"Item costs more than 20")

        # increment counter
        counter += 1
    else:
        print(f"Item costs less than 20")


print(f"Cart contains {counter} items more than 20 Rs.")



"""
Problem 2: Product Filter & Search

"""

# Given a list of products, implement:
# Search by name (partial match)    name = phone
def search_by_name(cart: list, name: str): # type hinting -> FastAPI, GenAI, Pydantic
    name = name.lower()

    # loop
    for item in cart:
        # item: dict
        # find the name value
        item_name = item["name"]

        # comparison
        if name in item_name.lower():
            print(f'Match found: {item_name}')
            return item_name


products = [
    {"id": 1, "price": 999, "category": "Electronics", "name": "iPhone 15"},    # <--
    {"id": 2, "name": "Samsung TV", "price": 1500, "category": "Electronics"},  # <--
    {"id": 3, "name": "Nike Shoes", "price": 120, "category": "Fashion"}
]

search_by_name(products, 'tv')

# Find all the prices
prices = []
# loop
# item['price']
# prices.append(^)

# Sort by price (ascending/descending)
prices = [999, 1500, 120]
prices.sort(reverse=False)
print(prices)








