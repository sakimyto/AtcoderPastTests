def resolve():
    a, b, c, x, y = map(int, input().split())
    if x == y:
        ans = min(x * a + y * b, x * 2 * c)
    elif x > y:
        ans = min(x * a + y * b, x * 2 * c, y * 2 * c + (x - y) * a)
    else:
        ans = min(x * a + y * b, y * 2 * c, x * 2 * c + (y - x) * b)
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
