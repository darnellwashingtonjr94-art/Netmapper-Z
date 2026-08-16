import whois
from utils.logger import get_logger

logger = get_logger()

def get_whois(domain):
    try:
        w = whois.whois(domain)
        return {
            "registrar": w.registrar,
            "creation_date": str(w.creation_date),
            "emails": w.emails if isinstance(w.emails, list) else [w.emails]
        }
    except Exception as e:
        logger.error(f"WHOIS lookup failed for {domain}: {e}")
        return {}
