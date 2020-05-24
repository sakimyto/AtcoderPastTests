def resolve():
    sx, sy, tx, ty = map(int, input().split())
    diff_x = tx - sx
    diff_y = ty - sy
    ans = 'U' * diff_y + 'R' * diff_x + 'D' * diff_y + 'L' * diff_x
    ans += 'LU' + 'U' * diff_y + 'R' * diff_x + 'RDRD' + 'D' * diff_y + 'L' * diff_x + 'LU'
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
        input = """0 0 1 2"""
        output = """UURDDLLUUURRDRDDDLLU"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """-2 -2 1 1"""
        output = """UURRURRDDDLLDLLULUUURRURRDDDLLDL"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
