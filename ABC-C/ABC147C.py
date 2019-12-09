def resolve():
    n = int(input())
    a = []
    dict = []
    for i in range(n):
        a.append(int(input()))
        dict.append([list(map(int, input().split())) for _ in [0] * a[-1]])
    cnt = 0
    for i in range(2 ** n):
        flag = 0
        c = ('0' * n + bin(i)[2:])[-n:]
        for i in range(n):
            if c[i] == '0':
                continue
            for j, k in dict[i]:
                if (k == 1 and c[j - 1] == '0') or (k == 0 and c[j - 1] == '1'):
                    flag = 1
                    break
        if flag == 1:
            continue
        cnt = max(cnt, c.count('1'))
    print(cnt)


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
2 1
1
1 1
1
2 0"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
2
2 1
3 0
2
3 1
1 0
2
1 1
2 0"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
1
2 0
1
1 0"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
