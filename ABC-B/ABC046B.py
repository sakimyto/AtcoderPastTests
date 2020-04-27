def resolve():
    n, k = map(int, input().split())
    ans = k
    for _ in range(n - 1):
        ans *= k - 1
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
        input = """2 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 10"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 8"""
        output = """322828856"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
