import dns.zone
import dns.query
from utils.logger import get_logger

logger = get_logger()

def test_zone_transfer(domain, nameserver):
    try:
        logger.info(f"Testing zone transfer (AXFR) for {domain} on {nameserver}")
        z = dns.zone.from_xfr(dns.query.xfr(nameserver, domain))
        return list(z.nodes.keys())
    except Exception as e:
        logger.warning(f"Zone transfer failed or blocked for {domain}: {e}")
        return []
