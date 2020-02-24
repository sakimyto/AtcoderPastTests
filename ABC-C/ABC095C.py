def resolve():
    a, b, c, x, y = map(int, input().split())
    if a + b < c * 2:
        ans = a * x + b * y
    else:
        p1_cnt = max(x, y)
        p1_price = p1_cnt * c * 2
        p2_cnt = min(x, y)
        if p2_cnt == x:
            p2_price = p2_cnt * c * 2 + (y - x) * b
        else:
            p2_price = p2_cnt * c * 2 + (x - y) * a
        ans = min(p1_price, p2_price)
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
        input = """1500 2000 1600 3 2"""
        output = """7900"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1500 2000 1900 3 2"""
        output = """8500"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1500 2000 500 90000 100000"""
        output = """100000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
