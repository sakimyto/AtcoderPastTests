n, k = map(int, input().split())
h = [int(i) for i in input().split()]
ans = 0
for j in h:
    if j >= k:
        ans += 1
print(ans)
