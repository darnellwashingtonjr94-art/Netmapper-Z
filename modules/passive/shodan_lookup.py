import requests
from config.settings import SHODAN_API_KEY
from utils.logger import get_logger

logger = get_logger()

def query_shodan(ip_address):
    if not SHODAN_API_KEY:
        logger.warning("Shodan API key not configured. Skipping query.")
        return {}
        
    url = f"https://api.shodan.io/shodan/host/{ip_address}?key={SHODAN_API_KEY}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        logger.error(f"Shodan query failed for {ip_address}: {e}")
    return {}
