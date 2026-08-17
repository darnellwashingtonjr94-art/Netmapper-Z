import nmap
from utils.logger import get_logger

logger = get_logger()

def scan_vulnerabilities(target, script_category="vuln"):
    try:
        nm = nmap.PortScanner()
        logger.info(f"Executing NSE script category '{script_category}' on {target}")
        nm.scan(hosts=target, arguments=f"--script {script_category}")
        
        vuln_results = {}
        for host in nm.all_hosts():
            vuln_results[host] = nm[host].get('script', {})
        return vuln_results
    except Exception as e:
        logger.error(f"Vulnerability scan failed on {target}: {e}")
        return {}
