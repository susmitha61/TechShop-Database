from entity.exceptions.invalid_data_exception import InvalidDataException

class Customer:
    def __init__(self, customer_id: int, first_name: str, last_name: str, email: str, phone: str, address: str):
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone = phone
        self.__address = address

    def register(self, db_connector):
        query = "INSERT INTO customers (CustomerID, FirstName, LastName, Email, Phone, Address) VALUES (?, ?, ?, ?, ?, ?)"
        try:
            db_connector.execute_query(query, (
                self.customer_id,
                self.first_name,
                self.last_name,
                self.email,
                self.phone,
                self.address
            ))
            print("Customer registered successfully.")
        except Exception as e:
            if "UNIQUE constraint failed" in str(e) or "duplicate key" in str(e):
                print("Error: Email already exists.")
            else:
                print(f"Error registering customer: {e}")

    def calculate_total_orders(self, db_connector):
        query = "SELECT COUNT(*) FROM Orders WHERE CustomerID = ?"
        result = db_connector.fetch_query(query, (self.__customer_id,))
        return result[0][0] if result else 0

    def get_customer_details(self) -> str:
        return f"ID: {self.__customer_id}, Name: {self.__first_name} {self.__last_name}, Email: {self.__email}, Phone: {self.__phone}, Address: {self.__address}"

    def update_customer_info(self, email=None, phone=None, address=None):
        if email:
            if "@" not in email:
                raise InvalidDataException("Invalid email address.")
            self.__email = email
        if phone:
            self.__phone = phone
        if address:
            self.__address = address

    # Getters
    @property
    def customer_id(self):
        return self.__customer_id

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def email(self):
        return self.__email

    @property
    def phone(self):
        return self.__phone

    @property
    def address(self):
        return self.__address

    @staticmethod
    def read_customers(db_connector):
        query = "SELECT * FROM customers"
        return db_connector.fetch_query(query)

    def update_customer(self, db_connector, customer_id):
        query = "UPDATE customers SET Email=?, Phone=?, Address=? WHERE CustomerID=?"
        db_connector.execute_query(query, (self.email, self.phone,self.address, customer_id))
        print("Customer updated successfully.")
    @staticmethod
    def delete_customer(db_connector, customer_id):
        query = "DELETE FROM customers WHERE id=?"
        db_connector.execute_query(query, (customer_id,))
        print("Customer deleted successfully.")

    def __str__(self):
        return f"{self.__first_name} {self.__last_name} ({self.__email}) {self.__phone} {self.__address}"