Test = int(input())

while Test!=0:
    Test -= 1
    num_input = str(input())
    ok = True;
    for i in range(0, len(num_input)):
        if (num_input[i]!='4' and num_input[i]!='7'):
            ok = False
            break
    if (ok):
        print("YES\n")
    else:
        print("NO\n")
