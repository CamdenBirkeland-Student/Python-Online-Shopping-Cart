class ItemToPurchase:
    def __init__(self, name="none", price=0.0, quantity=0, description="none"):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description

    def print_item_cost(self):
        """Print the item name, quantity, and subtotal cost."""
        cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${cost:.2f}")