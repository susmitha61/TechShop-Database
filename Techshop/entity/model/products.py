from entity.exceptions.invalid_data_exception import InvalidDataException

class Product:
    def __init__(self, product_id: int, product_name: str, description: str, price: float,category: str,stock_quantity:int):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__description = description
        self.__price = price
        self.__category = category
        self.__stock_quantity = stock_quantity

    def add_product(self, db_connector):
        query = """
        INSERT INTO Products (ProductID, ProductName, Description, Price, Category, StockQuantity)
        VALUES (?, ?, ?, ?, ?, ?)"""
        db_connector.execute_query(query, (
            self.product_id, self.product_name, self.description,
            self.price, self.category, self.stock_quantity
        ))
        print("Product added successfully.")

    @staticmethod
    def read_products(db_connector):
        query = "SELECT * FROM Products"
        return db_connector.fetch_query(query)

    def update_product(self, db_connector, product_id):
        query = """
        UPDATE Products
        SET ProductName=?, Price=?, Description=?, Category=?, StockQuantity=?
        WHERE ProductID=?"""
        db_connector.execute_query(query, (
            self.product_name, self.price, self.description,
            self.category, self.stock_quantity, product_id
        ))
        print("Product updated successfully.")

    @staticmethod
    def delete_product(db_connector, product_id):
        query = "DELETE FROM Products WHERE ProductID=?"
        db_connector.execute_query(query, (product_id,))
        print("Product deleted successfully.")

    def get_product_details(self):
        return (f"ID: {self.__product_id}, Name: {self.__product_name}, Description: {self.__description}, "
                f"Price: {self.__price}, Category: {self.__category}, Stock: {self.__stock_quantity}")

    def update_product_info(self, price=None, description=None, category=None, stock_quantity=None):
        if price is not None:
            if price < 0:
                raise InvalidDataException("Price cannot be negative.")
            self.__price = price
        if description:
            self.__description = description
        if category:
            self.__category = category
        if stock_quantity is not None:
            self.__stock_quantity = stock_quantity

    def is_product_in_stock(self, db_connector):
        query = "SELECT StockQuantity FROM Products WHERE ProductID = ?"
        result = db_connector.fetch_query(query, (self.__product_id,))
        return result[0][0] > 0 if result else False

    # Getters
    @property
    def product_id(self):
        return self.__product_id

    @property
    def product_name(self):
        return self.__product_name

    @property
    def description(self):
        return self.__description

    @property
    def price(self):
        return self.__price

    @property
    def category(self):
        return self.__category

    @property
    def stock_quantity(self):
        return self.__stock_quantity


class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if any(p.product_id == product.product_id for p in self.products):
            raise ValueError("Duplicate product ID.")
        self.products.append(product)

    def update_product(self, product_id, updated_product):
        for i, product in enumerate(self.products):
            if product.product_id == product_id:
                self.products[i] = updated_product
                return
        raise ValueError("Product not found.")

    def remove_product(self, product_id):
        for i, product in enumerate(self.products):
            if product.product_id == product_id:
                del self.products[i]
                return
        raise ValueError("Product not found or has existing orders.")

    def search_products(self, criteria):
        return [p for p in self.products if criteria.lower() in p.product_name.lower()]
