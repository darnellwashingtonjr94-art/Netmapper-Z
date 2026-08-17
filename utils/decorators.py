import time
from functools import wraps
from utils.logger import get_logger

logger = get_logger()

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logger.info(f"Function '{func.__name__}' executed in {end - start:.2f} seconds.")
        return result
    return wrapper
