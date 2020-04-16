def resolve():
    h, w = map(int, input().split())
    sss = [list(input()) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if sss[i][j] == '#':
                continue
            else:
                cnt = 0
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        if 0 <= i + y < h and 0 <= j + x < w:
                            if sss[i + y][j + x] == '#':
                                cnt += 1

                        sss[i][j] = str(cnt)
    for s in sss:
        print(''.join(s))


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
        input = """3 5
.....
.#.#.
....."""
        output = """11211
1#2#1
11211"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 5
#####
#####
#####"""
        output = """#####
#####
#####"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 6
#####.
#.#.##
####.#
.#..#.
#.##..
#.#..."""
        output = """#####3
#8#7##
####5#
4#65#2
#5##21
#4#310"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
