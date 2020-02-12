def resolve():
    n, k = map(int, input().split())
    x = [0 for _ in range(n)]
    for i in range(1, n + 1):
        tmp = 1
        m = i
        while (m < k):
            tmp /= 2
            m *= 2
        x[i - 1] = tmp
    print(sum(x) / n)


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
        input = """3 10"""
        output = """0.145833333333"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100000 5"""
        output = """0.999973749998"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
