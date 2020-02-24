def resolve():
    n = int(input())
    min_f = 10
    for i in range(1, n + 1):
        if i ** 2 > n:
            break
        if n % i != 0:
            continue
        min_seq = max(len(str(i)), len(str(n // i)))
        if min_seq < min_f:
            min_f = min_seq
    print(min_f)


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
        input = """10000"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1000003"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9876543210"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
