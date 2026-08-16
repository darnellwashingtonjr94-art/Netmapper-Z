#!/usr/bin/env python3
import argparse
from core.engine import run_scan
from utils.logger import setup_logger

def main():
    parser = argparse.ArgumentParser(description="Netmapper-Z: Hybrid Reconnaissance Framework")
    parser.add_argument("-d", "--domain", required=True, help="Target domain (e.g., example.com)")
    parser.add_argument("-m", "--mode", choices=["passive", "active"], default="passive", help="Scan mode")
    parser.add_argument("-p", "--ports", default="top-100", help="Ports to scan in active mode")
    parser.add_argument("-o", "--output", default="report.json", help="Output JSON file name")
    
    args = parser.parse_args()
    logger = setup_logger()
    
    logger.info(f"Starting Netmapper-Z against {args.domain} (Mode: {args.mode})")
    run_scan(args.domain, args.mode, args.ports, args.output)

if __name__ == "__main__":
    main()
