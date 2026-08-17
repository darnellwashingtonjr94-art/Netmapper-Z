import time
from utils.logger import get_logger

logger = get_logger()

class RateLimiter:
    def __init__(self, delay_seconds=1.5):
        self.delay = delay_seconds

    def wait(self):
        time.sleep(self.delay)
