list_operator  = ["+", "-", "*", "/"]

def isNum(s):
    for i in range(0, len(s)):
        if (not '0'<=s[i]<='9'):
            return False
    return True

def cal_num(c, a, b):
    if (c == "+"):
        return a+b
    elif (c == "-"):
        return a-b
    elif (c == "*"):
        return a*b
    elif (c == "/"):
        return a/b

Test = int(input())

while (Test != 0):
    Test -= 1
    exp = str(input()).rstrip()
    list1 = exp.split()
    list2 = []
    ok = True
    for s in list1:
        if (isNum(s)):
            list2.append(int(s))
        elif (s in list_operator):
            if len(list2)<2:
                ok = False
                break
            a = list2[-2]
            b = list2[-1]
            list2.pop(-1)
            list2.pop(-1)
            if (s == '/' and b == 0):
                ok = False
                break
            num = cal_num(s, a, b)
            list2.append(num)
        else:
            ok = False
            break
    if (ok == False):
        print("INVALID")
        continue
    if (len(list2)>1):
        print("INVALID")
        continue
    print(f"{list2[0]:.5f}")