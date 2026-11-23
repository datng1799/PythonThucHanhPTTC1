n = int(input())

for _ in range(n):
    s = str(input())
    s2 =""
    for j in range(0, len(list)):
        s2 = s2+ "".join(reversed(list[j]))+" "
    s2.rstrip()
    print(s2)