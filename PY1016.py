Test = int(input())

while (Test!=0):
    Test -=1
    s_inp = str(input().strip())
    if (len(s_inp)<2):
        print("NO")
        continue
    if (s_inp[-2]=='8' and s_inp[-1]=='6'):
        print("YES")
    else:
        print("NO")