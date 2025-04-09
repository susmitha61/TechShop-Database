from util.db_connector import DatabaseConnector
from entity.model.products import Product
from entity.model.orders import Order
from entity.model.order_details import OrderDetail
from entity.model.inventory import Inventory
from entity.model.inventory import InventoryManager
from entity.exceptions.incomplete_order_exception import IncompleteOrderException  # ✅ Fixes exception
from entity.exceptions.insufficient_stock_exception import InsufficientStockException  # ✅ Fixes exception


def main():
    db = None  # declare db early
    try:
        db = DatabaseConnector('HP-15EF2XXX', 'Techshop')
        db.open_connection()

        # 1. Create customer object
        """ customer = Customer(
            12,
            "Alice",
            "Smith",
            "alicejohn@example.com",
            "1234567890",
            "123 Main Street"
        )
   
        # 2. Optional: Register customer
        # customer.register(db)

        # 3. Update contact info
        print("\nUpdating customer info...")
        customer.update_customer_info("alice.smith@newmail.com", "9876543210", "456 New Avenue")
        customer.update_customer(db, customer.customer_id)

        # 4. Print updated details
        print("\nUpdated Customer Details:")
        print(customer.get_customer_details())

        # 5. Calculate orders
        print("\nCalculating total orders placed by the customer...")
        total_orders = customer.calculate_total_orders(db)
        print(f"Total Orders by Customer {customer.customer_id}: {total_orders}")


        # print("\nDeleting customer...")

        print("\n--- PRODUCT CRUD OPERATIONS ---")

        # CREATE
        print("Adding product to database...")
        product = Product(201, "Laptop", "High-performance laptop", 1299.99, "Electronics", 15)

        try:
            product.add_product(db)
            print("Product added.")
        except Exception as e:
            print(f"Error adding product: {e}")

        # READ
        print("\nFetching products from database...")
        products = Product.read_products(db)
        if not products:
            print("No products found in database.")
        else:
            for prod in products:
                print(
                    f"ID: {prod[0]}, Name: {prod[1]}, Desc: {prod[2]}, Price: {prod[3]}, Cat: {prod[4]}, Stock: {prod[5]}")

        # UPDATE
        print("\nUpdating product info...")
        product.update_product_info(price=1199.99, description="Discounted laptop", stock_quantity=10)
        product.update_product(db, product.product_id)

        # DELETE
        #print("\nDeleting product...")
        #Product.delete_product(db, product.product_id)
        #print("Product deleted.")
     # 1. Create / Add Order
        print("\n Placing new order...")
        customer = Customer(
            customer_id=1,
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            phone="1234567890",
            address="NYC"
        )
        order = Order(
            order_id=101,
            customer=customer,
            order_date=datetime.now().strftime("%Y-%m-%d"),
            total_amount=250.50
        )
        order.place_order(db)

        # 2. Read Orders
        print("\nReading all orders...")
        orders = Order.read_orders(db)
        for ord in orders:
            print(ord)

        # 3. Update Order
        print("\n Updating order total amount...")
        # Create a new Order object with updated total_amount
        updated_order = Order(
            order_id=101,
            customer=customer,
            order_date=datetime.now().strftime("%Y-%m-%d"),
            total_amount=299.99
        )
        updated_order.update_order(db, order_id=101)

        #4. Delete Order (optional)
       # Order.delete_order(db, order_id=101) 

        #  1. Create Customer, Product, and Order
        customer = Customer(
            customer_id=1,
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            phone="1234567890",
            address="NYC"
        )
        product = Product(
            product_id=1,
            product_name="Gaming Mouse",
            description="RGB 7-button gaming mouse",
            price=150.0,
            category="Gaming",
            stock_quantity=5
        )
        order = Order(
            order_id=206,
            customer=customer,
            order_date=datetime.now().strftime("%Y-%m-%d"),
            total_amount=150.0
        )

        # Place the order (if not already placed)
       # order.place_order(db)


        order_detail = OrderDetail(
            order_detail_id=12,
            order=order,
            product=product,
            quantity=2
        )

        order_detail.add_order_detail(db)

        #3. Display Order Detail Info
        print("\n Order Detail Info:")
        print(order_detail.get_order_detail_info())

        # 4. Update Quantity
        print("\n Updating quantity to 5...")
        order_detail.update_quantity(5)
        print("Updated Quantity:", order_detail.quantity)

        #  5. Apply Discount
        print("\n Applying 10% discount...")
        discounted_total = order_detail.add_discount(10)
        print("Total after discount:", discounted_total)
    """
        inventory_manager = InventoryManager()

        # Example Product
        product = Product(
            product_id=1,
            product_name="Phone",
            description="Smartphone",
            price=500,
            category="Electronics",
            stock_quantity=10
        )

        # Create Inventory Manager and add new inventory
        inventory_manager = InventoryManager()

        inventory_item = Inventory(inventory_id=101, product=product, quantity_in_stock=10)
        inventory_manager.add_inventory(inventory_item)

        # Read inventory from DB
        print("\n--- Inventory List ---")
        inventory_list = Inventory.read_inventory(db)
        for item in inventory_list:
            print(item)

        inventory_item.add_to_inventory(5)
        inventory_item.update_inventory(db)
        db.commit()  # Commit the transaction to save changes to the database

        print("\nInventory updated successfully.")
        inventory_item.insert_inventory_to_db(db)  # Insert into DB after update

        # Final read of inventory
        print("\n--- Final Inventory ---")
        inventory_list = Inventory.read_inventory(db)
        for item in inventory_list:
            print(item)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        db.close_connection()

if __name__ == "__main__":
    main()