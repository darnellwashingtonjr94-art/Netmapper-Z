# 1. Ensure the directory structure and init files exist locally
mkdir -p modules/active
touch modules/__init__.py modules/active/__init__.py

# 2. Re-create the port_scan.py file to make sure it's physically there
cat << 'EOF' > modules/active/port_scan.py
import nmap
from utils.logger import get_logger

logger = get_logger()

def run_nmap(target, ports):
    try:
        nm = nmap.PortScanner()
        port_arg = "-F" if ports == "top-100" else f"-p {ports}"
        
        logger.info(f"Scanning {target} with args: -sS -sV {port_arg}")
        nm.scan(hosts=target, arguments=f"-sS -sV {port_arg}")
        
        scan_data = []
        for host in nm.all_hosts():
            for proto in nm[host].all_protocols():
                ports_list = nm[host][proto].keys()
                for port in ports_list:
                    state = nm[host][proto][port]['state']
                    service = nm[host][proto][port]['name']
                    scan_data.append({"port": port, "state": state, "service": service})
        return scan_data
    except Exception as e:
        logger.error(f"Nmap scan failed on {target}: {e}")
        return []
EOF

# 3. Force git to track and push the files
git add modules/
git commit -m "Force track modules and port_scan.py for CI"
git push origin main
