def resolve():
    n = int(input())
    aaa = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        if aaa[i - 1] > aaa[i]:
            ans += aaa[i - 1] - aaa[i]
            aaa[i] = aaa[i - 1]
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
2 1 5 4 3"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
3 3 3 3 3"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
