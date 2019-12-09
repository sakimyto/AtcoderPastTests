def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = sum(b)
    for i in range(n - 1):
        if a[i] + 1 == a[i + 1]:
            ans += c[a[i] - 1]
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
        input = """3
3 1 2
2 5 4
3 6"""
        output = """14"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
2 3 4 1
13 5 8 24
45 9 15"""
        output = """74"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
1 2
50 50
50"""
        output = """150"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
