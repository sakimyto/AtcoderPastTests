def resolve():
    abc = list(map(int, input().split()))
    abc.sort()
    abc2 = abc[:]

    if sum(abc) % 2 != 3 * abc[2] % 2:
        abc2[2] += 1

    print((abc2[2] * 3 - sum(abc)) // 2)


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
        input = """2 5 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 6 3"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """31 41 5"""
        output = """23"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
