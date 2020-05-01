def resolve():
    n = int(input())
    aaa = list(map(int, input().split()))
    ans = 0
    for a in aaa:
        while a % 3 == 2 or a % 2 == 0:
            a -= 1
            ans += 1
    print(ans)

    # 1サイクル自分で見つける発想をもつとよい
    # n = int(input())
    # a = map(int, input().split())
    # ans = 0
    # l_seq = [3, 0, 1, 0, 1, 2]
    # for i in a:
    #     ans += l[i % 6]
    # print(ans)


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

    def test_入力例1(self):
        input = """3
5 8 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """9
1 2 3 4 5 6 7 8 9"""
        output = """8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
