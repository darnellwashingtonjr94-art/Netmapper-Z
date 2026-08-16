import json
from utils.logger import get_logger

logger = get_logger()

def generate_report(data_dict, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(data_dict, f, indent=4)
    except IOError as e:
        logger.error(f"Failed to write report to {filename}: {e}")
