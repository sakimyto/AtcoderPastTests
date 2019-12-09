def resolve():
    n, k, q = map(int, input().split())
    a = list(input() for i in range(q))
    dict = {}
    for i in range(q):
        if a[i] in dict.keys():
            dict[a[i]] += 1
        else:
            dict[a[i]] = 1

    for j in range(1, n+1):
        if str(j) in dict.keys():
            if k - q + int(dict[str(j)]) > 0:
                print('Yes')
            else:
                print('No')
        else:
            print('No')


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
        input = """6 3 4
3
1
3
2"""
        output = """No
No
Yes
No
No
No"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 5 4
3
1
3
2"""
        output = """Yes
Yes
Yes
Yes
Yes
Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 13 15
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
5
8
9
7
9"""
        output = """No
No
No
No
Yes
No
No
No
Yes
No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
