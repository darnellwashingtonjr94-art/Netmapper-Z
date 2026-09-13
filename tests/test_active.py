import sys
from pathlib import Path

# Add project root directory to sys.path so 'modules' imports resolve correctly
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import unittest
from unittest.mock import patch, Mock
from modules.active_port_scan import run_nmap


class TestActiveModules(unittest.TestCase):

    @patch('modules.active_port_scan.nmap.PortScanner')
    def test_run_nmap_success(self, mock_port_scanner):
        mock_instance = Mock()
        mock_instance.all_hosts.return_value = ['127.0.0.1']
        mock_instance.__getitem__.return_value = {
            'tcp': {80: {'state': 'open', 'name': 'http'}}
        }
        mock_port_scanner.return_value = mock_instance

        results = run_nmap('127.0.0.1', '80')
        self.assertIsInstance(results, list)


if __name__ == '__main__':
    unittest.main()
