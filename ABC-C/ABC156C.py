def resolve():
    import math
    n = int(input())
    xl = list(map(int, input().split()))
    xl_cnt = len(xl)
    xl_sum = sum(xl)
    xl_avg = xl_sum / xl_cnt
    xl_diff = map(lambda x: x - int(format(xl_avg, '.0f')), xl)
    xl_double = map(lambda x: x * x, xl_diff)
    print(sum(xl_double))

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
        input = """2
1 4"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
14 14 2 13 56 2 37"""
        output = """2354"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
