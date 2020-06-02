def resolve():
    from collections import Counter
    n = int(input())
    aaa = list(map(int, input().split()))
    cnt_a = Counter(aaa)
    ans = 0
    for key in cnt_a.keys():
        value = cnt_a[key]
        if key > value:
            ans += value
        elif key < value:
            ans += value - key
        else:
            continue
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
        input = """4
3 3 3 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
2 4 1 4 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
1 2 2 3 3 3"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1
1000000000"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """8
2 7 1 8 2 8 1 8"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
