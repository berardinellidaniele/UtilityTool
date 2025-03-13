import unittest
import os
from utils.file_ops import read, write

class TestFileOps(unittest.TestCase):
    def setUp(self):
        self.test_file = "test.txt"
        with open(self.test_file, "w") as f:
            f.write("test")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_read(self):
        self.assertEqual(read(self.test_file), "test")

    def test_write(self):
        write(self.test_file, "new content")
        self.assertEqual(read(self.test_file), "new content")

    def test_read_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            read("missing.txt")

if __name__ == "__main__":
    unittest.main()
