def resolve():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    max = 0
    for i in range(n - 1):
        if h[i] >= h[i + 1]:
            ans += 1
        else:
            if max < ans:
                max = ans
            ans = 0
    if max < ans:
        max = ans
    print(max)


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
        input = """5
10 4 8 7 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
4 4 5 6 6 5 5"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
1 2 3 4"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
