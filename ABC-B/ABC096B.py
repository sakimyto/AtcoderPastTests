def resolve():
    lst = list(map(int, input().split()))
    k = int(input())
    for _ in range(k):
        n = lst.index(max(lst))
        lst[n] = lst[n] * 2
    print(sum(lst))


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
        input = """5 3 11
1"""
        output = """30"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3 4
2"""
        output = """22"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
