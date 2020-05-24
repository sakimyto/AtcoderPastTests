def resolve():
    n = int(input())
    a = [0] * n
    for _ in range(n):
        a[int(input()) - 1] += 1
    x, y = -1, -1
    for i in range(n):
        if a[i] == 0:
            x = i + 1
        elif a[i] == 2:
            y = i + 1
    if (x == -1 or y == -1):
        print("Correct")
    else:
        print(y, x)


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
        input = """6
1
5
6
3
2
6"""
        output = """6 4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
5
4
3
2
7
6
1"""
        output = """Correct"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
