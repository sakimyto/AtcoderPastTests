def resolve():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if i + 1 != p[i]:
            cnt += 1
    if cnt <= 2:
        print("YES")
    else:
        print("NO")


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
5 2 3 4 1"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
2 4 3 5 1"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
1 2 3 4 5 6 7"""
        output = """YES"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
