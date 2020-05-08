def resolve():
    n = int(input())
    aaa = [int(input()) for _ in range(n)]
    max_a = sorted(aaa)[-1]
    second_a = sorted(aaa)[-2]
    for a in aaa:
        if a == max_a:
            print(second_a)
        if a != max_a:
            print(max_a)

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
1
4
3"""
        output = """4
3
4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
5
5"""
        output = """5
5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
