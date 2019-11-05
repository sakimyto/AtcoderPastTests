def resolve():
    n = int(input())
    i = 1
    ans = n
    while i * i <= n:
        j, m = divmod(n, i)
        if m == 0:
            ans = min(ans, i + j - 2)
        i += 1
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
        input = """10"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """50"""
        output = """13"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10000000019"""
        output = """10000000018"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
