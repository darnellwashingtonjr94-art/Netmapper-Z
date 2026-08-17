import requests
from utils.logger import get_logger

logger = get_logger()

def search_github_leaks(domain):
    url = f"https://api.github.com/search/code?q={domain}+filename:.env"
    headers = {"Accept": "application/vnd.github.v3+json"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json().get("items", [])
    except Exception as e:
        logger.error(f"GitHub leak search failed: {e}")
    return []
