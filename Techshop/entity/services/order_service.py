from entity.exceptions.concurrency_exception import ConcurrencyException

# Simulated database of orders for demonstration purposes
orders_db = {
    1: {"status": "processing", "updated_by": None},
    2: {"status": "completed", "updated_by": None},
}


def order_is_being_updated(order_id):
    """
    Check if the order is currently being updated.

    Args:
        order_id (int): The ID of the order to check.

    Returns:
        bool: True if the order is being updated, False otherwise.
    """
    order = orders_db.get(order_id)
    if order and order["status"] == "processing":
        return True
    return False


def update_order(order_id, new_data):
    """
    Update the order with the given ID.

    Args:
        order_id (int): The ID of the order to update.
        new_data (dict): The new data to update the order with.

    Raises:
        ConcurrencyException: If the order is currently being updated by another user.
    """
    if order_is_being_updated(order_id):
        raise ConcurrencyException("Order is currently being updated by another user.")

    # Proceed with updating the order logic here
    orders_db[order_id].update(new_data)
    orders_db[order_id]["updated_by"] = "current_user"  # Simulate the user who updated the order

def __init__(self, order_manager, inventory_manager):
    self.order_manager = order_manager
    self.inventory_manager = inventory_manager
def create_order(self, order):
    self.order_manager.add_order(order)

def update_order_status(self, order_id, status):
    self.order_manager.update_order_status(order_id, status)

def remove_canceled_order(self, order_id):
     self.order_manager.remove_canceled_order(order_id)