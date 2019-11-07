def resolve():
    n = int(input())
    lis = [111, 222, 333, 444, 555, 666, 777, 888, 999]
    for i in range(9):
        if n > lis[i]:
            continue
        else:
            print(lis[i])
            break


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
        input = """111"""
        output = """111"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """112"""
        output = """222"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """750"""
        output = """777"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
