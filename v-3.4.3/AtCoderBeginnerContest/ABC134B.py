def resolve():
    n, d = map(int, input().split())
    if n % (2 * d + 1) == 0:
        ans = n // (2 * d + 1)
    else:
        ans = n // (2 * d + 1) + 1
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
        input = """6 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """14 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """20 4"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
