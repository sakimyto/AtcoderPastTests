def resolve():
    a = input()
    b = input()
    if len(a) > len(b):
        print(a)
    else:
        print(b)

import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例1(self):
        input = """isuruu
isleapyear"""
        output = """isleapyear"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """ttttiiiimmmmeeee
time"""
        output = """ttttiiiimmmmeeee"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()