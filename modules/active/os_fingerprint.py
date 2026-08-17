import nmap
from utils.logger import get_logger

logger = get_logger()

def detect_os(target):
    try:
        nm = nmap.PortScanner()
        logger.info(f"Running OS detection fingerprint on {target}")
        nm.scan(hosts=target, arguments="-O --osscan-guess")
        
        os_matches = []
        if target in nm.all_hosts() and 'osmatch' in nm[target]:
            for match in nm[target]['osmatch']:
                os_matches.append({
                    "name": match.get("name"),
                    "accuracy": match.get("accuracy")
                })
        return os_matches
    except Exception as e:
        logger.error(f"OS fingerprinting failed for {target}: {e}")
        return []
