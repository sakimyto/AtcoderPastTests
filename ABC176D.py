def resolve():
    from collections import deque

    h, w = map(int, input().split())
    ch, cw = map(lambda x: int(x) + 1, input().split())
    dh, dw = map(lambda x: int(x) + 1, input().split())
    s = [["#"] * (w + 4) for _ in range(2)] + [["#"] * 2 + list(input()) + ["#"] * 2 for _ in range(h)] + [
        ["#"] * (w + 4) for _ in range(2)]
    m1 = ((-1, 0), (0, -1), (0, 1), (1, 0))
    m2 = [(i, j) for i in range(-2, 3) for j in range(-2, 3) if abs(i) + abs(j) > 1]
    a = deque([(ch, cw)])
    b = deque()
    i = 0
    while a:
        while a:
            ah, aw = a.popleft()
            if s[ah][aw] != ".":
                continue
            b.append((ah, aw))
            s[ah][aw] = i
            for bh, bw in m1:
                bh, bw = ah + bh, aw + bw
                if s[bh][bw] == ".":
                    a.append((bh, bw))
        while b:
            ah, aw = b.popleft()
            for bh, bw in m2:
                bh, bw = ah + bh, aw + bw
                if s[bh][bw] == ".":
                    a.append((bh, bw))
        i += 1
    ans = s[dh][dw]
    print(ans if ans != "." else -1)


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
1 1
4 4
..#.
..#.
.#..
.#.."""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 4
1 4
4 1
.##.
####
####
.##."""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 4
2 2
3 3
....
....
....
...."""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """4 5
1 2
2 5
#.###
####.
#..##
#..##"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
