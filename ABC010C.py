def resolve():
    txa, tya, txb, tyb, t, v = map(int, input().split())
    n = int(input())
    xxyy = [list(map(int, input().split())) for _ in range(n)]
    ans = 'NO'
    for x, y in xxyy:
        d = ((x - txa) ** 2 + (y - tya) ** 2) ** 0.5 + ((x - txb) ** 2 + (y - tyb) ** 2) ** 0.5
        if t >= d / v:
            ans = 'YES'
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
        input = """1 1 8 2 2 4
1
4 5"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """1 1 8 2 2 6
1
4 5"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """1 1 8 2 2 5
1
4 5"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """7 7 1 1 3 4
3
8 1
1 7
9 9"""
        output = """YES"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
