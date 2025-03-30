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