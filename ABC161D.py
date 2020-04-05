def resolve():
    k = int(input())

    a = []

    def dfs(x):
        if x > 3234566667:
            return
        a.append(x)
        for i in range(10):
            if abs(x % 10 - i) <= 1:
                dfs(x * 10 + i)

    for i in range(1, 10):
        dfs(i)

    a = sorted(a)
    print(a[k - 1])


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
        input = """15"""
        output = """23"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """13"""
        output = """21"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """100000"""
        output = """3234566667"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
