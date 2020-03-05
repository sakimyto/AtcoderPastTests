def resolve():
    a, b, k = map(int, input().split())
    ans = []
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            ans.append(i)
    print(ans[-k])


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
        input = """8 12 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100 50 4"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 1 1"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
