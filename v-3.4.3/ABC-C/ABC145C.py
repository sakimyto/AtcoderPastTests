def resolve():
    import math
    n = int(input())
    lst = [[int(i) for j in input().split()] for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            if lst[i][0] == lst[j][0] and lst[i][1] == lst[j][1]:
                continue
            else:
                a = (lst[i][0] - lst[j][0]) ** 2 + (lst[i][1] - lst[j][1]) ** 2
            ans += math.sqrt(a)
    print(ans / n)


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
        input = """3
0 0
1 0
0 1"""
        output = """2.2761423749"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
-879 981
-866 890"""
        output = """91.9238815543"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8
-406 10
512 859
494 362
-955 -475
128 553
-986 -885
763 77
449 310"""
        output = """7641.9817824387"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
