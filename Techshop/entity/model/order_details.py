# File: entity/model/order_details.py
from entity.model.orders import Order
from entity.model.products import Product
from entity.exceptions.incomplete_order_exception import IncompleteOrderException

class OrderDetail:
    def __init__(self, order_detail_id: int, order: Order, product: Product, quantity: int):
        self.__order_detail_id = order_detail_id
        self.__order = order
        self.__product = product
        self.__quantity = quantity

    def __str__(self):
        return f"OrderDetail [ID: {self.order_detail_id}, Product: {self.product.product_name}, Quantity: {self.quantity}]"

    def add_order_detail(self, db_connector):
        query = "INSERT INTO OrderDetails (OrderDetailID, OrderID, ProductID, Quantity) VALUES (?, ?, ?, ?)"
        db_connector.execute_query(query, (
            self.order_detail_id,
            self.order.order_id,
            self.product.product_id,
            self.quantity
        ))
        print("Order detail added successfully.")

    def calculate_subtotal(self) -> float:
        return self.__product.price * self.__quantity

    def get_order_detail_info(self) -> str:
        return (
            f"Order Detail ID: {self.__order_detail_id}, "
            f"Product: {self.__product.get_product_details()}, "
            f"Quantity: {self.__quantity}, "
            f"Subtotal: {self.calculate_subtotal()}"
        )

    def update_quantity(self, new_quantity: int) -> None:
        if new_quantity <= 0:
            raise IncompleteOrderException("Quantity must be positive.")
        self.__quantity = new_quantity

    def add_discount(self, discount: float) -> float:
        if discount < 0:
            raise IncompleteOrderException("Discount cannot be negative.")
        subtotal = self.calculate_subtotal()
        discount_amount = subtotal * (discount / 100)
        return subtotal - discount_amount

    # Getters
    @property
    def order_detail_id(self):
        return self.__order_detail_id

    @property
    def order(self):
        return self.__order

    @property
    def product(self):
        return self.__product

    @property
    def quantity(self):
        return self.__quantity
# OrderManager Class
class OrderManager:
    def __init__(self):
        self.orders = []

    def add_order(self, order_details):
        self.orders.append(order_details)

    @staticmethod
    def validate_order_details(order_details, inventory_manager):
        for detail in order_details:
            inventory_item = inventory_manager.get_item(detail.product_id)
            if inventory_item.quantity < detail.quantity:
                raise ValueError("Product not available in sufficient quantity.")