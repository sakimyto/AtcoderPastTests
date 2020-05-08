def resolve():
    import math
    x = int(input())
    while True:
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                break
        else:
            print(x)
            break
        x += 1


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
        input = """20"""
        output = """23"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """99992"""
        output = """100003"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
