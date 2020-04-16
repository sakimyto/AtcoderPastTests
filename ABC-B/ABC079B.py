def resolve():
    n = int(input())

    def defs(n):
        l0 = 2
        l1 = 1
        ans = 1
        if n == 1:
            return ans
        else:
            for i in range(2, n + 1):
                ans = l0 + l1
                l0 = l1
                l1 = ans
            return ans

    print(defs(n))


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
        input = """5"""
        output = """11"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """86"""
        output = """939587134549734843"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
