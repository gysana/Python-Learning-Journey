# ============================================================

# ASSIGNMENT 1: CAFE MENU AND ORDER MANAGEMENT

# ============================================================

# QUESTION 1:

# The cafe needs to store the item name, price, and availability.

#

# 1. Item name:

# We use the String (str) data type because the item name

# contains text.

# Example:

# item_name = "Cappuccino"

#

# 2. Price:

# We use the Float (float) data type because prices can

# contain decimal values.

# Example:

# price = 5.00

#

# 3. Availability:

# We use the Boolean (bool) data type because an item can

# either be available (True) or unavailable (False).

# Example:

# available = True

#

# Example of storing menu item details:

#

# item_name = "Cappuccino"

# price = 5.00

# available = True

# QUESTION 2(a):

# Arithmetic operators can be used to calculate the total

# cost of an order.

#

# Formula:

# Total Cost = Price * Quantity

#

# Example:

#

# price = 5.00

# quantity = 2

# total_cost = price * quantity

# print(total_cost)

#

# Output:

# 10.0

#

# If a customer orders multiple items, their individual

# costs can be added together.

#

# Example:

#

# cappuccino = 5.00 * 2

# sandwich = 4.00 * 1

# total_cost = cappuccino + sandwich

#

# Output:

# 14.0

# ============================================================

# QUESTION 3:

# Write a Python program that:

# a. Asks the user to input the menu item and quantity.

# b. Calculates the total cost using fixed prices.

# c. Displays a formatted message showing the purchase

# and total cost.

# ============================================================

# MENU

# Dictionary is used to store the menu items, their prices,

# and their availability.

menu = {
"cappuccino": {
"price": 5.00,
"available": True
},
"coffee": {
    "price": 3.00,
    "available": True
},

"tea": {
    "price": 2.50,
    "available": True
},

"sandwich": {
    "price": 4.00,
    "available": True
},

"cake": {
    "price": 3.50,
    "available": False
}
}

# DISPLAY MENU

print("================================")
print(          menu                      )
print("================================")

for item in menu:
   price = menu[item]["price"]
   available = menu[item]["available"]
if available:
    print(item.title(), "- $", format(price, ".2f"), "- Available")
else:
    print(item.title(), "- $", format(price, ".2f"), "- Not Available")


# GET CUSTOMER NAME
customer_name = input("\nEnter customer name: ")

# GET MENU ITEM FROM CUSTOMER

item = input("Enter menu item: ").lower()

# CHECK WHETHER THE ITEM EXISTS IN THE MENU

if item in menu:


# CHECK WHETHER THE ITEM IS AVAILABLE

 if menu[item]["available"]:

    # GET QUANTITY

    quantity = int(input("Enter quantity: "))


    # GET PRICE OF THE SELECTED ITEM

    price = menu[item]["price"]


    # CALCULATE TOTAL COST

    total_cost = price * quantity


    # DISPLAY ORDER DETAILS

    print("\n================================")
    print("         ORDER DETAILS          ")
    print("================================")

    print(
        f"Customer {customer_name} is buying "
        f"{quantity} {item}(s). "
        f"Total cost: ${total_cost:.2f}"
    )


# IF ITEM IS NOT AVAILABLE

 else:
    print("\nSorry, this item is currently not available.")


# IF ITEM DOES NOT EXIST

else:
  print("\nSorry, this item is not on the menu.")

# ============================================================

# END OF ASSIGNMENT

# ============================================================
 