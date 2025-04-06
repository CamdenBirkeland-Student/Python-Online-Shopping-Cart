import json
import os

from item_to_purchase import ItemToPurchase
from shopping_cart import ShoppingCart

def print_menu(cart):
    """
    Displays the menu and processes user input until 'q' is chosen.
    """
    user_choice = ""
    while user_choice != 'q':
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("s - Save cart to file")
        print("l - Load cart from file")
        print("q - Quit")

        user_choice = input("Choose an option:\n").strip()

        if user_choice == 'a':
            add_item_to_cart(cart)
        elif user_choice == 'r':
            remove_item_from_cart(cart)
        elif user_choice == 'c':
            change_item_quantity(cart)
        elif user_choice == 'i':
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        elif user_choice == 'o':
            print("OUTPUT SHOPPING CART")
            cart.print_total()
        elif user_choice == 's':
            save_cart(cart)  
        elif user_choice == 'l':
            load_cart(cart)  
        elif user_choice == 'q':
            # Quit the menu loop
            break
        else:
            # Invalid choice; let the loop prompt again
            print("Invalid option. Please try again.")

def add_item_to_cart(cart):
    print("ADD ITEM TO CART")
    name = input("Enter the item name:\n")
    description = input("Enter the item description:\n")
    price = float(input("Enter the item price:\n"))
    quantity = int(input("Enter the item quantity:\n"))
    # Create a new ItemToPurchase and add it to the cart
    new_item = ItemToPurchase(name, price, quantity, description)
    cart.add_item(new_item)


def remove_item_from_cart(cart):
    print("REMOVE ITEM FROM CART")
    name = input("Enter name of item to remove:\n")
    cart.remove_item(name)


def change_item_quantity(cart):
    print("CHANGE ITEM QUANTITY")
    name = input("Enter the item name:\n")
    quantity = int(input("Enter the new quantity:\n"))
    # We only modify quantity here, but could also let user modify price/desc if desired.
    # (Set price=0.0, description="none" so they remain unchanged)
    modified_item = ItemToPurchase(name=name, quantity=quantity)
    cart.modify_item(modified_item)

def save_cart(cart, filename="cart_data.json"):
    """
    Saves the ShoppingCart data to a JSON file.
    """
    # Prepare a dictionary with all needed cart info
    cart_data = {
        "customer_name": cart.customer_name,
        "current_date": cart.current_date,
        "items": []
    }

    # Convert each ItemToPurchase into a dictionary
    for item in cart.cart_items:
        item_dict = {
            "item_name": item.item_name,
            "item_description": item.item_description,
            "item_price": item.item_price,
            "item_quantity": item.item_quantity
        }
        cart_data["items"].append(item_dict)

    # Write the data to a JSON file
    with open(filename, "w") as f:
        json.dump(cart_data, f, indent=4)

    print(f"Cart saved to {filename}")

def load_cart(cart, filename="cart_data.json"):
    """
    Loads ShoppingCart data from a JSON file into the provided cart.
    """
    if not os.path.exists(filename):
        print(f"No saved cart found at {filename}.")
        return

    with open(filename, "r") as f:
        cart_data = json.load(f)

    # Clear out any existing items from the cart
    cart.cart_items = []

    # Update cart’s attributes
    cart.customer_name = cart_data.get("customer_name", "none")
    cart.current_date = cart_data.get("current_date", "January 1, 2020")

    # Reconstruct each ItemToPurchase
    for item_dict in cart_data.get("items", []):
        item = ItemToPurchase(
            name=item_dict["item_name"],
            description=item_dict["item_description"],
            price=item_dict["item_price"],
            quantity=item_dict["item_quantity"]
        )
        cart.add_item(item)

    print(f"Cart loaded from {filename}")

def main():
    # First, gather the customer's name and today's date
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print()

    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")

    # Create a new ShoppingCart object
    cart = ShoppingCart(customer_name, current_date)

    # Call the menu function
    print_menu(cart)


if __name__ == "__main__":
    main()
