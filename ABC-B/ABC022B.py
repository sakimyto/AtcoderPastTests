def resolve():
    # これTLEになるのどこに時間かかってるんだ？
    # n = int(input())
    # n_list = []
    # ans = 0
    # for _ in range(n):
    #     tmp = int(input())
    #     if tmp in n_list:
    #         ans += 1
    #     else:
    #         n_list.append(tmp)
    # print(ans)

    n = int(input())
    aaa = [int(input()) for _ in range(n)]
    aa = set(aaa)
    print(len(aaa) - len(aa))



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
        input = """5
1
2
3
2
1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """11
3
1
4
1
5
9
2
6
5
3
5"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
