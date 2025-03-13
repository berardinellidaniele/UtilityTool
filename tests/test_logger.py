import unittest
import logging
import os
from utils.logger import get_logger

class TestLogger(unittest.TestCase):
    def test_logger(self):
        logger = get_logger()
        logger.info("test log")
        self.assertTrue(os.path.exists("logs/filemanager.log"))

if __name__ == "__main__":
    unittest.main()
