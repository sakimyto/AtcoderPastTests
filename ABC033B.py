def resolve():
    n = int(input())
    sss = [''] * n
    ppp = [0] * n
    for i in range(n):
        s, p = map(str, input().split())
        sss[i] = s
        ppp[i] = int(p)
    print(sss[ppp.index(max(ppp))] if max(ppp) > sum(ppp) / 2 else 'atcoder')


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
        input = """4
unagi 20
usagi 13
snuke 42
smeke 7"""
        output = """snuke"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
a 10
b 20
c 30
d 40
e 100"""
        output = """atcoder"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """14
yasuzuka 3340
uragawara 4032
oshima 2249
maki 2614
kakizaki 11484
ogata 10401
kubiki 9746
yoshikawa 5142
joetsu 100000
nakago 4733
itakura 7517
kiyosato 3152
sanwa 6190
nadachi 3169"""
        output = """joetsu"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
