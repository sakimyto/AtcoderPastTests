def resolve():
    n, t = map(int, input().split())
    cost = 1e9
    for i in range(n):
        cn, tn = map(int, input().split())
        if tn <= t and cost > cn:
            cost = cn
    if cost == 1e9:
        print('TLE')
    else:
        print(cost)


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
        input = """3 70
7 60
1 80
4 50"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 3
1 1000
2 4
3 1000
4 500"""
        output = """TLE"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 9
25 8
5 9
4 10
1000 1000
6 1"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
