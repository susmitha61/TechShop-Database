from datetime import datetime
from sortedcontainers import SortedList

from entity.model.products import Product
from entity.exceptions.insufficient_stock_exception import InsufficientStockException

class Inventory:
    def __init__(self, inventory_id: int, product: Product, quantity_in_stock: int, last_stock_update=None):
        self.__inventory_id = inventory_id
        self.__product = product  # Instance of Product class
        self.__quantity_in_stock = quantity_in_stock
        self.__last_stock_update = last_stock_update or datetime.now()
        self.product_id = product.product_id  # Convenience attribute for lookup

    def insert_inventory_to_db(self, db_connector):
        query = """
            INSERT INTO Inventory (InventoryID, ProductID, QuantityInStock, LastStockUpdate)
            VALUES (?, ?, ?, ?)
        """
        db_connector.execute_query(query, (
            self.inventory_id,
            self.product.product_id,
            self.quantity_in_stock,
            self.last_stock_update
        ))
        print("New inventory record inserted into database.")

    def __str__(self):
        return f"Inventory ID: {self.inventory_id}, Product: {self.product.product_name}, Stock: {self.quantity_in_stock}"

    def update_inventory(self, db_connector):
        query = "UPDATE Inventory SET QuantityInStock = ?, LastStockUpdate = GETDATE() WHERE InventoryID = ?"
        db_connector.execute_query(query, (self.quantity_in_stock, self.inventory_id))
        db_connector.commit()  # Commit the transaction to make sure changes are saved
        print("Inventory updated successfully.")

    @staticmethod
    def read_inventory(db_connector):
        query = "SELECT InventoryID, ProductID, QuantityInStock, LastStockUpdate FROM Inventory"
        return db_connector.fetch_query(query)

    def get_product(self):
        return self.product

    def get_quantity_in_stock(self):
        return self.quantity_in_stock

    def add_to_inventory(self, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        self.__quantity_in_stock += quantity
        self.__last_stock_update = datetime.now()

    def remove_from_inventory(self, quantity: int) -> None:
        if quantity > self.__quantity_in_stock:
            raise InsufficientStockException("Not enough stock available.")
        self.__quantity_in_stock -= quantity
        self.__last_stock_update = datetime.now()

    def update_stock_quantity(self, new_quantity: int) -> None:
        if new_quantity < 0:
            raise ValueError("Stock quantity cannot be negative.")
        self.__quantity_in_stock = new_quantity
        self.__last_stock_update = datetime.now()

    def is_product_available(self, quantity_to_check: int) -> bool:
        return self.__quantity_in_stock >= quantity_to_check

    def get_inventory_value(self) -> float:
        return self.__product.price * self.__quantity_in_stock

    def list_low_stock_products(self, threshold: int) -> bool:
        return self.__quantity_in_stock < threshold

    def list_out_of_stock_products(self) -> bool:
        return self.__quantity_in_stock == 0

    def list_all_products(self) -> str:
        return f"Product: {self.__product.get_product_details()}, Quantity: {self.__quantity_in_stock}"

    # Getters
    @property
    def inventory_id(self):
        return self.__inventory_id

    @property
    def product(self):
        return self.__product

    @property
    def quantity_in_stock(self):
        return self.__quantity_in_stock

    @property
    def last_stock_update(self):
        return self.__last_stock_update


class InventoryManager:
    def __init__(self):
        self.inventory = SortedList()

    def add_inventory(self, inventory_item):
        self.inventory.add(inventory_item)

    def update_inventory(self, product_id, quantity):
        for item in self.inventory:
            if item.product_id == product_id:
                item.add_to_inventory(quantity)
                return
        raise ValueError("Product not found in inventory.")

    def read_inventory(self):
        return list(self.inventory)

    def remove_inventory(self, product_id, quantity):
        for item in self.inventory:
            if item.product.product_id == product_id:
                item.remove_from_inventory(quantity)
                print(f"Removed {quantity} units from inventory.")
                return
        raise ValueError("Product not found in inventory.")
