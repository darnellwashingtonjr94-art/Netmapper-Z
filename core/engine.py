from modules.passive.crt_sh import fetch_subdomains
from modules.passive.whois_lookup import get_whois
from modules.active.port_scan import run_nmap
from reports.json_report import generate_report
from utils.logger import get_logger

logger = get_logger()

def run_scan(domain, mode, ports, output_file):
    results = {"target": domain, "whois": {}, "subdomains": [], "live_hosts": {}}
    
    logger.info("Running WHOIS lookup...")
    results["whois"] = get_whois(domain)
    
    logger.info("Querying Certificate Transparency logs for subdomains...")
    results["subdomains"] = fetch_subdomains(domain)
    
    if mode == "active":
        logger.info("Initiating active Nmap scan on discovered targets...")
        for sub in results["subdomains"]:
            results["live_hosts"][sub] = run_nmap(sub, ports)
            
    generate_report(results, output_file)
    logger.info(f"Scan complete. Results saved to {output_file}")
