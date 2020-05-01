def resolve():
    n = int(input())
    rrr = [int(input()) for _ in range(n)]
    rrr.sort(reverse=True)
    sum_r2 = 0
    for num, r in enumerate(rrr):
        if num % 2 == 0:
            sum_r2 += r ** 2
        else:
            sum_r2 -= r ** 2
    print(sum_r2 * 3.141592653589793)


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
        input = """3
1
2
3"""
        output = """18.8495559215"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """6
15
2
3
7
6
9"""
        output = """508.938009881546"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
