def resolve():
    w, h, n = map(int, input().split())
    xyas = [list(map(int, input().split())) for _ in range(n)]
    min_x = 0
    max_x = w
    min_y = 0
    max_y = h
    for xya in xyas:
        if xya[2] == 1:
            min_x = max(min_x, xya[0])
        elif xya[2] == 2:
            max_x = min(max_x, xya[0])
        elif xya[2] == 3:
            min_y = max(min_y, xya[1])
        else:
            max_y = min(max_y, xya[1])
    if ((max_x - min_x) < 0) or ((max_y - min_y) < 0):
        print(0)
    else:
        print((max_x - min_x) * (max_y - min_y))


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
        input = """5 4 2
2 1 1
3 3 4"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 4 3
2 1 1
3 3 4
1 4 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 10 5
1 6 1
4 1 3
6 9 4
9 4 2
3 1 3"""
        output = """64"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
