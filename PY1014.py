Test = int(input())

while (Test !=0):
    Test -= 1
    num_s = str(input())
    chr = ''
    count = 0
    res = ""
    for i in range(0, len(num_s)):
        if ('A'<=num_s[i]<='Z'):
            chr = num_s[i]
        if ('1'<=num_s[i]<='9'):
            count = ord(num_s[i])-ord('0')
            for j in range(0, count):
                res += str(chr)
    print(res)