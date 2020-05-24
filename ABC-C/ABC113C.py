def resolve():
    n, m = map(int, input().split())
    ppyy = [list(map(int, input().split())) for _ in range(m)]
    order = [{}] * (n + 1)
    cnt = [1] * (n + 1)
    for p, y in sorted(ppyy, key=lambda x: x[1]):
        order[p].update({y: cnt[p]})
        cnt[p] += 1
    for p, y in ppyy:
        cnt[p] += 1
        print(str(format(p, '06')) + str(format(order[p][y], '06')))


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
1 32
2 63
1 12"""
        output = """000001000002
000002000001
000001000001"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 3
2 55
2 77
2 99"""
        output = """000002000001
000002000002
000002000003"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
