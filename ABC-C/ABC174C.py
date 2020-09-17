def resolve():
    k = int(input())
    aaa = [0] * k
    aaa[0] = 7 % k
    for i in range(1, k):
        aaa[i] = (aaa[i - 1] * 10 + 7) % k
    ans = -1
    for j in range(k):
        if aaa[j] == 0:
            ans = j + 1
            break
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
        input = """101"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """999983"""
        output = """999982"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
