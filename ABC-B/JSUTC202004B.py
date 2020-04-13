def resolve():
    n = int(input())
    xc = []
    for _ in range(n):
        x, c = input().split()
        xc.append([int(x), c])
    xc = sorted(xc)

    for i in xc:
        if i[1] == 'R':
            print(int(i[0]))
    for j in xc:
        if j[1] == 'B':
            print(int(j[0]))


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
        input = """4
10 B
6 R
2 R
4 B"""
        output = """2
6
4
10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
5 B
7 B"""
        output = """5
7"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
