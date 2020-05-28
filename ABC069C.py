def resolve():
    n = int(input())
    aaa = list(map(int, input().split()))
    odd = 0
    even = 0
    even4 = 0
    for a in aaa:
        if a % 4 == 0:
            even4 += 1
        elif a % 2 == 0:
            even += 1
        else:
            odd += 1
    if odd == 0:
        print('Yes')
    else:
        if even4 == 0:
            print('No')
        else:
            if even == 0:
                print('Yes' if even4 >= odd - 1 else 'No')
            else:
                print('Yes' if even4 >= odd else 'No')


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
        input = """3
1 10 100"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 2 3 4"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
1 4 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2
1 1"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """6
2 7 1 8 2 8"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
