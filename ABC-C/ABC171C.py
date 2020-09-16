def resolve():
    n = int(input())
    alphabets = [chr(i) for i in range(ord('a'), ord('a') + 26)]
    ans = ''
    while n > 0:
        n -= 1
        ans += alphabets[n % 26]
        n //= 26
    print(ans[::-1])


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
        input = """2"""
        output = """b"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """27"""
        output = """aa"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """123456789"""
        output = """jjddja"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
