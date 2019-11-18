def resolve():
n = int(input())
s = input()
if n % 2 == 1:
    print('No')
else:
    t = int(n / 2)
    if s[:t] == s[t:]:
        print('Yes')
    else:
        print('No')


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
        input = """6
abcabc"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
abcadc"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
z"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
