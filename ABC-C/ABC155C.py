def resolve():
    n = int(input())
    dict = {}
    for _ in range(n):
        s = input()
        if s in dict:
            dict[s] += 1
        else:
            dict[s] = 0
    max_val = max(dict.values())
    max_list = [k for k, v in dict.items() if v == max_val]
    max_list.sort()
    for i in max_list:
        print(i)


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
        input = """7
beat
vet
beet
bed
vet
bet
beet"""
        output = """beet
vet"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8
buffalo
buffalo
buffalo
buffalo
buffalo
buffalo
buffalo
buffalo"""
        output = """buffalo"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
bass
bass
kick
kick
bass
kick
kick"""
        output = """kick"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """4
ushi
tapu
nichia
kun"""
        output = """kun
nichia
tapu
ushi"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
