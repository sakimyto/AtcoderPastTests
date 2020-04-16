def resolve():
    n = int(input())
    ans = 0
    for i in range(n):
        l, r = map(int, input().split())
        ans += r - l + 1
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

    def test_入力例_1(self):
        input = """1
24 30"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
6 8
3 3"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
