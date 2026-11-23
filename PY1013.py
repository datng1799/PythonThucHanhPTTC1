Test = int(input())

while (Test!=0):
    Test -=1
    ok = True
    num_s = str(input())
    for i in range(0, len(num_s)-1):
        pre = ord(num_s[i]) - ord('0')
        lst = ord(num_s[i+1]) - ord('0')
        if (pre>lst):
            ok = False
            break
    if (ok):
        print("YES")
    else: print("NO")