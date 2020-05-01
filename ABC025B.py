def resolve():
    n, a, b = map(int, input().split())
    sds = [list(map(str, input().split())) for _ in range(n)]
    ans = 0
    for sd in sds:
        tmp1 = sd[0]
        tmp2 = int(sd[1])
        if tmp2 <= a:
            ans = ans + a if tmp1 == 'East' else ans - a
        elif b <= tmp2:
            ans = ans + b if tmp1 == 'East' else ans - b
        else:
            ans = ans + tmp2 if tmp1 == 'East' else ans - tmp2
    if ans > 0:
        print('East ' + str(ans))
    elif ans < 0:
        print('West ' + str(-ans))
    else:
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

    def test_入力例1(self):
        input = """3 5 10
East 7
West 3
West 11"""
        output = """West 8"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3 3 8
West 6
East 3
East 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """5 25 25
East 1
East 1
West 1
East 100
West 1"""
        output = """East 25"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
