def resolve():
    n = int(input())
    ans = 10 ** 5
    for i in range(1, n + 1):
        tmp = n - i * (n // i) + abs(i - (n // i))
        ans = min(ans, tmp)
    print(ans)


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
        input = """26"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """41"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """100000"""
        output = """37"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
