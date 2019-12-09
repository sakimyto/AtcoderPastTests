def resolve():
    s = list(input())
    t = list(input())
    ctn = 0
    for i in range(3):
        if s[i] == t[i]:
            ctn += 1
    print(ctn)


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
    def test_入力例_1(self):
        input = """CSS
CSR"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """SSR
SSR"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """RRR
SSS"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()