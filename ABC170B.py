def resolve():
    x, y = map(int, input().split())
    ans = 'No'
    for i in range(x + 1):
        if i * 2 + (x - i) * 4 == y:
            ans = 'Yes'
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
        input = """3 8"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 100"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 2"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """100 202"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
