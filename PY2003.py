Test = int(input())

while (Test != 0):
    Test -= 1
    num_s = str(input())
    k = int(input())
    a = list(map(int, num_s.split()))
    out = []
    if (k<=0 or k>=len(a)):
        print("INVALID")
        continue
    for i in range(0, len(a) ,k):
        out.append(a[i:i+k])
    for i in range(0, len(out)):
        print(out[i], end=" ")
    print()