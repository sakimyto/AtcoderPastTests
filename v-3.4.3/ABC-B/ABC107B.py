def resolve():
    h, w = map(int, input().split())
    lis = []
    for i in range(h):
        lis.append(input())

    row = [False] * h
    col = [False] * w
    for i in range(h):
        for j in range(w):
            if lis[i][j] == '#':
                row[i] = True
                col[j] = True

    for i in range(h):
        if row[i]:
            s = ''
            for j in range(w):
                if col[j]:
                    s += lis[i][j]
            print(s)


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
        input = """4 4
##.#
....
##.#
.#.#"""
        output = """###
###
.##"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3
#..
.#.
..#"""
        output = """#..
.#.
..#"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 5
.....
.....
..#..
....."""
        output = """#"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """7 6
......
....#.
.#....
..#...
..#...
......
.#..#."""
        output = """..#
#..
.#.
.#.
#.#"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
