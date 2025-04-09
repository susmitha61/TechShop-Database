from entity.exceptions.io_exception import IOException

def log_error(message: str):
    try:
        with open("log.txt", "a") as log_file:
            log_file.write(message + "\n")
    except Exception:
        raise IOException("Failed to write to log file.")
