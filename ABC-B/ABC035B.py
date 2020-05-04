def resolve():
    s = input()
    t = int(input())
    l_cnt = s.count('L')
    r_cnt = s.count('R')
    u_cnt = s.count('U')
    d_cnt = s.count('D')
    q_cnt = s.count('?')
    x = abs(r_cnt - l_cnt)
    y = abs(u_cnt - d_cnt)
    if t == 1:
        print(x + y + q_cnt)
    else:
        print(x + y - q_cnt if x + y >= q_cnt else (x + y + q_cnt) % 2)


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
        input = """UL?
1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """UD?
1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """UUUU?DDR?LLLL
1"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """UULL?
2"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
