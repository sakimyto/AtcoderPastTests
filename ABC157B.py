def resolve():
    a = [list(map(int, input().split())) for _ in range(3)]
    for i in range(int(input())):
        b = int(input())
        for j in range(3):
            for k in range(3):
                if a[j][k] == b:
                    a[j][k] = 0
    ans = 'No'
    for i in range(3):
        if a[i][0] == a[i][1] == a[i][2] == 0:
            ans = 'Yes'
        if a[0][i] == a[1][i] == a[2][i] == 0:
            ans = 'Yes'
    if a[0][0] == a[1][1] == a[2][2] == 0:
        ans = 'Yes'
    if a[2][0] == a[1][1] == a[0][2] == 0:
        ans = 'Yes'
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
        input = """84 97 66
79 89 11
61 59 7
7
89
7
87
79
24
84
30"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """41 7 46
26 89 2
78 92 8
5
6
45
16
57
17"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """60 88 34
92 41 43
65 73 48
10
60
43
88
11
48
73
65
41
92
34"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
