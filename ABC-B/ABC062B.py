def resolve():
    h, w = map(int, input().split())
    aaa = [list(map(str, input().split())) for _ in range(h)]
    for i, aw in enumerate(aaa):
        aw.insert(0, '#')
        aw.append('#')
        aaa[i] = aw
    aaa.insert(0, ['#' * (w + 2)])
    aaa.append(['#' * (w + 2)])

    for aw in aaa:
        print(''.join(aw))


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
        input = """2 3
abc
arc"""
        output = """#####
#abc#
#arc#
#####"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 1
z"""
        output = """###
#z#
###"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
