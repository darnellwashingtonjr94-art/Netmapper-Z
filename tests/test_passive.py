import unittest
from unittest.mock import patch, Mock
from modules.passive.whois_lookup import get_whois

class TestPassiveModules(unittest.TestCase):
    
    @patch('modules.passive.whois_lookup.whois.whois')
    def test_get_whois_success(self, mock_whois):
        mock_w = Mock()
        mock_w.registrar = "Test Registrar"
        mock_w.creation_date = "2020-01-01"
        mock_w.emails = ["admin@example.com"]
        mock_whois.return_value = mock_w
        
        result = get_whois("example.com")
        self.assertEqual(result["registrar"], "Test Registrar")
        self.assertIn("admin@example.com", result["emails"])

if __name__ == '__main__':
    unittest.main()
