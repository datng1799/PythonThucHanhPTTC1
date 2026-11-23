n = int(input())

dic = {}

for i in range(0, n):
    s1 = str(input())
    list1 = s1.split()
    for j in range(1, len(list1)):
        dic[list1[j]] = list1[0]

m = int(input())
for i in range(0, m):
    s2 = str(input())
    print(f"{s2} {dic[s2]}")