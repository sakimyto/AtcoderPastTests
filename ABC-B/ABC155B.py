def resolve():
    n = int(input())
    l = list(map(int, input().split()))
    ans = 'APPROVED'
    for i in l:
        if i % 2 == 0:
            if i % 3 != 0 and i % 5 != 0:
                ans = 'DENIED'
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
        input = """5
6 7 9 10 31"""
        output = """APPROVED"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
28 27 24"""
        output = """DENIED"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
