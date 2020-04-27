def resolve():
    n, m = map(int, input().split())
    aaa = [input() for _ in range(n)]
    bbb = [input() for _ in range(m)]
    ans = False
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            flag = True
            for k in range(m):
                for l in range(m):
                    if aaa[i + k][j + l] != bbb[k][l]:
                        flag = False
            if flag:
                ans = True
    if ans:
        print('Yes')
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
        input = """3 2
#.#
.#.
#.#
#.
.#"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 1
....
....
....
....
#"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
