def resolve():
    n = int(input())
    aaa = [int(input()) for _ in range(n)]
    num = 1
    ans = -1
    for i in range(n):
        num = aaa[num - 1]
        if num == 2:
            ans = i + 1
            break
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
3
1
2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
3
4
1
2"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
3
3
4
2
4"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
