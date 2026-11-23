Test = int(input())

while (Test != 0):
    Test -=1
    num_s = str(input())
    ok = True
    for i in range(0, len(num_s)):
        if (num_s[i]!='0' and num_s[i]!='1' and num_s[i]!='2'):
            ok = False
            break
    if (ok):
        print("YES")
    else:
        print("NO")