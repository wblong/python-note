import unittest
import sys


class MyTestClass(unittest.TestCase):
    def test_name(self):
        self.fail("Not implemented")
def main():
    MyTestClass()

if __name__ == "__main__":
    sys.exit(int(main() or 0))