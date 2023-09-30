"""
Issues found:
- Unused Variables:
The variable total_items was declared but never used in the code.
Removed the unused variable to clean up the code.
- Incorrect Data Type
In the CART list, the price of 'Item C' was provided as a string ('8.49') instead of a float.
- Function Name
The function display_total had a capital 'T' in its name, which does not follow the Python convention for function naming.
- Missing Docstrings
There were no docstrings to provide documentation for the functions.
"""
def calculate_total(carts):
    """
    Calculate the total price of items in the shopping cart.

    Args:
        cart (list of dict): List of items in the cart, where each item is a dictionary with a 'price' key.

    Returns:
        float: The total price of items in the cart.
    """
    total = 0
    for i in carts:
        total += i['price']
    return total

def display_total(total):
    """
    Display the total price.

    Args:
        total (float): The total price to be displayed.
    """
    print("Total price: " + str(total))

cart = [
    {'name': 'Item A', 'price': 10.99},
    {'name': 'Item B', 'price': 5.99},
    {'name': 'Item C', 'price': 8.49}
]

for item in cart:
    print(f"Item: {item['name']} - Price: ${item['price']}")

shopping_cart_total = calculate_total(cart)
display_total(shopping_cart_total)
