import pyodbc

# Database connection configuration
server = 'localhost'
database = 'Techshop'

try:
    # Establish connection using Windows Authentication
    conn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'Trusted_Connection=yes;'
    )

    print("✅ Connection successful.\n")
    cursor = conn.cursor()
    # Update description for ProductID = 12
    update_query = """
            UPDATE Products
            SET Description = ?
            WHERE ProductID = ?
        """
    update_data = ('Wireless speaker', 12)
    cursor.execute(update_query, update_data)

    conn.commit()
    print("✅ Products updated with category and stock quantity.\n")

    # Display updated products table
    cursor.execute("SELECT ProductID, ProductName, Category, StockQuantity FROM Products")
    rows = cursor.fetchall()
    print("Updated Products Table:")
    for row in rows:
        print(row)

    conn.close()
    print("\nConnection closed successfully.")

except Exception as e:
    print(f"=Connection failed: {e}")
