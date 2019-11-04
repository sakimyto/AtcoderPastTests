def resolve():
    a = int(input())
    ans = 0
    for i in range(a):
        ans += 10000 * (i + 1) / a
    print(int(ans))


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
        input = """6"""
        output = """35000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """91"""
        output = """460000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
