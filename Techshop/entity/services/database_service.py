from entity.exceptions.database_access_exception import DatabaseAccessException

def execute_query(query: str):
    try:
        # Assume db_connection is a database connection object
        db_connection.execute(query)
    except Exception:
        raise DatabaseAccessException("Database is offline or query failed.")
