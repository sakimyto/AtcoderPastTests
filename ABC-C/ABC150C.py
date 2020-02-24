def resolve():
    from itertools import permutations
    n = int(input())
    p = tuple(map(int, input().split()))
    q = tuple(map(int, input().split()))
    a, b = 0, 0
    for i, x in enumerate(permutations(range(1, n + 1), n)):
        if x == p:
            a = i
        if x == q:
            b = i
    print(abs(a - b))


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
1 3 2
3 1 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8
7 3 5 4 2 1 6 8
3 8 2 5 4 6 7 1"""
        output = """17517"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
1 2 3
1 2 3"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
