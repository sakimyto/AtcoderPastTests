def resolve():
    n = input()
    n = [int(ni) % 3 for ni in n]
    sum_n = sum(n) % 3
    ans = 0
    if sum_n == 0:
        pass
    elif sum_n == 1:
        if 1 in n and len(n) > 1:
            ans = 1
        elif n.count(2) >= 2 and len(n) > 2:
            ans = 2
        else:
            ans = -1
    else:
        if 2 in n and len(n) > 1:
            ans = 1
        elif n.count(1) >= 2 and len(n) > 2:
            ans = 2
        else:
            ans = -1
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
        input = """35"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """369"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6227384"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """11"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """1111122"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
