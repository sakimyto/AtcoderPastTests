def resolve():
    s = input()
    t = input()
    print('Yes' if sorted(s) < sorted(t, reverse=True) else 'No')


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
        input = """yx
axy"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """ratcode
atlas"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """cd
abc"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """w
ww"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """zzz
zzz"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
