# Restaurant Order Management
from collections import deque

# Class representing the restaurant's order queue
class RestaurantOrderQueue:
    def __init__(self):
        # Queue to hold orders in FIFO manner
        self.order_queue = deque()

    def add_order(self, order):
        """Add a new order to the kitchen's queue."""
        self.order_queue.append(order)
        print(f"Order '{order}' added to the queue.")

    def remove_order(self):
        """Remove the first order from the queue when completed."""
        if self.order_queue:
            completed_order = self.order_queue.popleft()
            print(f"Order '{completed_order}' completed and removed from the queue.")
            return completed_order
        else:
            print("No orders in the queue to remove.")
            return None

    def display_orders(self):
        """Display all current orders in the queue."""
        if self.order_queue:
            print("Current orders in the queue:")
            for order in self.order_queue:
                print(f"- {order}")
        else:
            print("No orders in the queue.")
# Example Usage:
order_system = RestaurantOrderQueue()

# Add some orders
order_system.add_order("Order 1: Burger and Fries")
order_system.add_order("Order 2: Pizza")
order_system.add_order("Order 3: Pasta")

# Display orders
order_system.display_orders()

# Remove completed orders
order_system.remove_order()
order_system.remove_order()

# Display remaining orders
order_system.display_orders()          
# Example Usage:
order_system = RestaurantOrderQueue()

# Add some orders
order_system.add_order("Order 1: Burger and Fries")
order_system.add_order("Order 2: Pizza")
order_system.add_order("Order 3: Pasta")

# Display orders
order_system.display_orders()

# Remove completed orders
order_system.remove_order()
order_system.remove_order()

# Display remaining orders
order_system.display_orders()


# Browsing History Management
class BrowsingHistory:
    def __init__(self):
        # Stack to represent browsing history
        self.history_stack = []

    def add_page(self, page):
        """Add a new page to the stack (representing visiting a new page)."""
        self.history_stack.append(page)
        print(f"page '{page}' added to browsing history.")

    def remove_page(self):
        """Remove the most recently added page from the stack."""
        if self.history_stack:
            removed_page = self.history_stack.pop()
            print(f"Page '{removed_page}' removed from browsing history.")
            return removed_page
        else:
            print("No pages to remove.")
            return None
    def pages_viewed(self):
        """Return the number of pages viewed in the current browsing session."""
        return len(self.history_stuck)
    
    def is_empty(self):
        """Check if the browsing history is empty."""
        return len(self.history_stuck) == 0

# Example usage:
history = BrowsingHistory()

# Add some pages
history.add_page("www.example.com")
history.add_page("www.wikipedia.org")
history.add_page("www.github.com")

# Check how many pages viewed
print(f"Pages viewed: {history.pages_viewed()}")

# Remove the last visited page
history.remove_page()

# Check if history is empty
if history.is_empty():
    print("Browsing history is empty.")
else:
    print(f"Pages viewed: {history.pages_viewed()}")
        
        
        