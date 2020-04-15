def resolve():
    n = int(input())
    s = list(map(str, input().split()))
    s = set(s)
    ans = ['Zero', 'One', 'Two', 'Three', 'Four']
    print(ans[len(s)])



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
        input = """6
G W Y P Y W"""
        output = """Four"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """9
G W W G P W P G G"""
        output = """Three"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8
P Y W G Y W Y Y"""
        output = """Four"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
