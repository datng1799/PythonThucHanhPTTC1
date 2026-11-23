def check_num(s):
    if len(s)<3:
        return True
    if len(s) == 3:
        if (s[0] == s[2]):
            return True
        else:
            return False
    for i in range(2, len(s), 2):
        if (s[i]!=s[i-2]):
            return False
    for i in range(3, len(s), 2):
        if (s[i]!=s[i-2]):
            return False
    return True

Test = int(input())

while (Test != 0):
    Test -=1
    num_s = str(input())
    if check_num(num_s):
        print("YES")
    else:
        print("NO")