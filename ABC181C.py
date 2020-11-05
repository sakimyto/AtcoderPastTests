def resolve():
    n = int(input())
    x = []
    y = []
    ans = 'No'

    for _ in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                x1 = x[i] - x[j]
                y1 = y[i] - y[j]
                x2 = x[j] - x[k]
                y2 = y[j] - y[k]
                if x1 * y2 == x2 * y1:
                    ans = 'Yes'
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
        input = """4
0 1
0 2
0 3
1 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """14
5 5
0 1
2 5
8 0
2 1
0 0
3 6
8 6
5 9
7 9
3 4
9 2
9 8
7 2"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9
8 2
2 3
1 3
3 7
1 0
8 8
5 6
9 7
0 1"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
