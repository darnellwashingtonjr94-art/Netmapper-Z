import requests
from utils.evasion import get_random_user_agent
from utils.logger import get_logger

logger = get_logger()

def fetch_subdomains(domain):
    url = f"https://crt.sh/?q=%.{domain}&output=json"
    headers = {"User-Agent": get_random_user_agent()}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            # Extract names and remove duplicates
            subdomains = set([entry["name_value"].lower() for entry in data])
            return list(subdomains)
    except Exception as e:
        logger.error(f"Failed to query crt.sh: {e}")
    
    return []
