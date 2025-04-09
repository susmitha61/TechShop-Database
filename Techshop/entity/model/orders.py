# File: entity/model/orders.py
from entity.exceptions.incomplete_order_exception import IncompleteOrderException


class Order:
    def __init__(self, order_id: int, customer, order_date=None, total_amount=0.0):
        self.__order_id = order_id
        self.__customer = customer  # Instance of Customer class
        self.__order_date = order_date
        self.__total_amount = total_amount
        self.__status = "Pending"  # Preserved from original
        self.product_id = None
        self.quantity = None

    def __str__(self):
        return f"Order ID: {self.order_id}, Customer: {self.customer.get_customer_details()}, Total Amount: {self.total_amount}, Order Date: {self.order_date}"

    def place_order(self, db_connector):
        query = "INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount) VALUES (?, ?, ?, ?)"
        db_connector.execute_query(query, (self.order_id, self.customer.customer_id, self.order_date, self.total_amount))
        print("Order placed successfully.")

    @staticmethod
    def read_orders(db_connector):
        query = "SELECT * FROM Orders"
        return db_connector.fetch_query(query)

    def update_order(self, db_connector, order_id):
        query = "UPDATE Orders SET CustomerID=?, OrderDate=?, TotalAmount=? WHERE OrderID=?"
        db_connector.execute_query(query, (self.customer.customer_id, self.order_date, self.total_amount, order_id))
        print("Order updated successfully.")

    @staticmethod
    def delete_order(db_connector, order_id):
        query = "DELETE FROM Orders WHERE OrderID=?"
        db_connector.execute_query(query, (order_id,))
        print("Order deleted successfully.")

    def calculate_total_amount(self, db_connector) -> float:
        query = "SELECT TotalAmount FROM Orders WHERE OrderID = ?"
        result = db_connector.fetch_query(query, (self.__order_id,))
        self.__total_amount = result[0][0] if result and result[0][0] is not None else 0.0
        return self.__total_amount

    def get_order_details(self) -> str:
        return (
            f"Order ID: {self.__order_id}, "
            f"Customer: {self.__customer.get_customer_details()}, "
            f"Total Amount: {self.__total_amount}, "
            f"Order Date: {self.__order_date}"
        )

    def update_order_status(self, status: str) -> None:
        valid_statuses = ["Pending", "Processing", "Shipped", "Delivered", "Canceled"]
        if status not in valid_statuses:
            raise IncompleteOrderException("Invalid status update.")
        self.__status = status

    def cancel_order(self, db_connector):
        query = "DELETE FROM Orders WHERE OrderID = ?"
        db_connector.execute_query(query, (self.__order_id,))
        print(f"Order {self.__order_id} has been canceled.")

    # Getters
    @property
    def order_id(self):
        return self.__order_id

    @property
    def customer(self):
        return self.__customer

    @property
    def order_date(self):
        return self.__order_date

    @property
    def total_amount(self):
        return self.__total_amount

    @property
    def status(self):
        return self.__status


class OrderManager:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def update_order(self, order_id, updated_order):
        for i, order in enumerate(self.orders):
            if order.order_id == order_id:
                self.orders[i] = updated_order
                return
        raise ValueError("Order not found.")

    def remove_order(self, order_id):
        for i, order in enumerate(self.orders):
            if order.order_id == order_id:
                del self.orders[i]
                return
        raise ValueError("Order not found.")

    def sort_orders_by_date(self, ascending=True):
        self.orders.sort(key=lambda x: x.order_date, reverse=not ascending)

    def filter_orders_by_customer(self, customer_id):
        return [order for order in self.orders if order.customer.customer_id == customer_id]

    @staticmethod
    def process_order(order, inventory_manager):
        for item in order.items:
            inventory_item = inventory_manager.get_item(item.product_id)
            if inventory_item.quantity < item.quantity:
                raise ValueError("Insufficient stock.")
            inventory_item.quantity -= item.quantity
