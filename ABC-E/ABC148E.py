def resolve():
    from itertools import accumulate
    n = int(input())
    n_list = []
    m = 1
    if n < 2 or n % 2 != 0:
        print(0)
    else:
        arr = np.arange(1, n).reshape(3, 5)
        while n > m:

        n_list.append(i)
        num = accumulate(n_list)
        print(len(str(num)) - len(str(num).rstrip('0')))


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
        input = """12"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000000000000000000"""
        output = """124999999999999995"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
