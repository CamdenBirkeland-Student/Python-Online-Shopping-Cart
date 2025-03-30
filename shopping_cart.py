class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        """
        Adds an ItemToPurchase object to the cart_items list.
        """
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        """
        Removes an item from cart_items by matching the item_name.
        If the item isn't found, prints an error message.
        """
        found = False
        for i, item in enumerate(self.cart_items):
            if item.item_name == item_name:
                del self.cart_items[i]
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_purchase):
        """
        Modifies an existing item's description, price, and/or quantity
        if the item exists in the cart. Otherwise, prints an error message.
        Only modify attributes if the parameter's values are not default.
        """
        found = False
        for cart_item in self.cart_items:
            if cart_item.item_name == item_to_purchase.item_name:
                # Found the item, now update any non-default values
                found = True
                if item_to_purchase.item_description != "none":
                    cart_item.item_description = item_to_purchase.item_description
                if item_to_purchase.item_price != 0.0:
                    cart_item.item_price = item_to_purchase.item_price
                if item_to_purchase.item_quantity != 0:
                    cart_item.item_quantity = item_to_purchase.item_quantity
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        """
        Returns the total quantity of all items in the cart.
        """
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

    def get_cost_of_cart(self):
        """
        Returns the total cost (sum of item_price * item_quantity for each item) 
        of all items in the cart.
        """
        total_cost = 0.0
        for item in self.cart_items:
            total_cost += (item.item_price * item.item_quantity)
        return total_cost

    def print_total(self):
        """
        Prints the customer name, current date, number of items, each line item cost, 
        and the total cost. If cart is empty, displays an appropriate message.
        """
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        num_items = self.get_num_items_in_cart()
        print(f"Number of Items: {num_items}")

        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
            total_cost = self.get_cost_of_cart()
            print(f"Total: ${total_cost:.2f}")

    def print_descriptions(self):
        """
        Prints the customer name, current date, and each item's description.
        """
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")