def resolve():
    n, k = map(int, input().split())
    s = 0
    for i in range(k, n + 2):
        s += i * (n - i + 1) + 1
    print(s % (10 ** 9 + 7))


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
        input = """3 2"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """200000 200001"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """141421 35623"""
        output = """220280457"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
