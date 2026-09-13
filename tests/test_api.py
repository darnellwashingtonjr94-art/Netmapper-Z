import sys
from pathlib import Path

# Add project root directory to sys.path so 'api' imports resolve correctly
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import unittest
from fastapi.testclient import TestClient
from api.main import app


class TestNetmapperAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_health_check(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})


if __name__ == '__main__':
    unittest.main()
