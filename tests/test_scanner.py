# test_scanner.py
import unittest
from app.scanner import perform_sast, perform_dast, perform_sca, perform_secret_scanning

class TestScanner(unittest.TestCase):
    def test_sast(self):
        result = perform_sast()
        self.assertEqual(result, "SAST results")

    def test_dast(self):
        result = perform_dast()
        self.assertEqual(result, "DAST results")

    def test_sca(self):
        result = perform_sca()
        self.assertEqual(result, "SCA results")

    def test_secret_scanning(self):
        result = perform_secret_scanning()
        self.assertEqual(result, "Secret Scanning results")

if __name__ == '__main__':
    unittest.main()
