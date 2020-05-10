def resolve():
    n, k = map(int, input().split())
    aaa = list(map(lambda x: int(x) - 1, input().split()))
    visited = [0] * n
    next_town = 0
    order = []
    while True:
        if visited[next_town]:
            break
        order.append(next_town)
        visited[next_town] = 1
        next_town = aaa[next_town]
    first_loop = len(order)
    offset = order.index(next_town)
    second_loop = first_loop - offset
    if k < first_loop:
        print(order[k] + 1)
    else:
        print(order[offset + (k - first_loop) % second_loop] + 1)


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
        input = """4 5
3 2 4 1"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 1
3 2 4 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 727202214173249351
6 5 2 5 3 2"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
