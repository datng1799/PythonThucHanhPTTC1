n = int(input())

cnt = {}
for _ in range(n):
    for w in input().split():
        cnt[w] = cnt.get(w, 0) +1
for w, c in sorted(cnt.items(), key = lambda p: (-p[1], p[0])):
    print(w, c)