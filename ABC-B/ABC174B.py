def resolve():
    n, d = map(int, input().split())
    ans = 0
    for _ in range(n):
        x, y = map(int, input().split())
        if (x ** 2 + y ** 2) ** 0.5 <= d:
            ans += 1
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
        input = """4 5
0 5
-2 4
3 4
4 -4"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """12 3
1 1
1 1
1 1
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """20 100000
14309 -32939
-56855 100340
151364 25430
103789 -113141
147404 -136977
-37006 -30929
188810 -49557
13419 70401
-88280 165170
-196399 137941
-176527 -61904
46659 115261
-153551 114185
98784 -6820
94111 -86268
-30401 61477
-55056 7872
5901 -163796
138819 -185986
-69848 -96669"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
