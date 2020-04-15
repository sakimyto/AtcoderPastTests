def resolve():
    # n = int(input())
    # dict = {}
    # for _ in range(n):
    #     s = input()
    #     if s not in dict:
    #         dict[s] = 0
    #     dict[s] += 1
    #
    # m = int(input())
    # for _ in range(m):
    #     t = input()
    #     if t not in dict:
    #         dict[t] = 0
    #     dict[t] -= 1
    # print(max(dict.values()) if max(dict.values()) > 0 else 0)

    # dict使うよりcountでさくっと言ったほうが楽そう
    n = int(input())
    s_list = [input() for _ in range(n)]
    m = int(input())
    t_list = [input() for _ in range(m)]
    ans = 0
    for s in s_list:
        score = s_list.count(s) - t_list.count(s)
        if ans < score:
            ans = score
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
apple
orange
apple
1
grape"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
apple
orange
apple
5
apple
apple
apple
apple
apple"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
voldemort
10
voldemort
voldemort
voldemort
voldemort
voldemort
voldemort
voldemort
voldemort
voldemort
voldemort"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """6
red
red
blue
yellow
yellow
red
5
red
red
yellow
green
blue"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
