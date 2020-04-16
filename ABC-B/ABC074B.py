def resolve():
    n = int(input())
    k = int(input())
    xxx = list(map(int, input().split()))
    ans = 0
    for x in xxx:
        ans += 2 * (x if k > 2 * x else k - x)
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
10
2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
9
3 6"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
20
11 12 9 17 12"""
        output = """74"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
