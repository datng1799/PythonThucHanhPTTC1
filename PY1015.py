Test = int(input())

while (Test != 0):
    Test -= 1
    num_s = str(input())
    char = num_s[0]
    count = 1
    res =""
    for i in range(1, len(num_s)):
        if (num_s[i] == char):
            count+=1
        else:
            res+= str(count)+str(char)
            char = num_s[i]
            count = 1
    res+= str(count)+str(char)
    print(res)