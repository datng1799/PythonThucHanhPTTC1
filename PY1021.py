
def sum_num(s1):
    s2 = s1[::-1]
    memory = 0
    length = len(s1)
    s3 =""
    for i in range(0, length):
        num_1 = ord(s1[i]) - ord('0')
        num_2 = ord(s2[i]) - ord('0')
        num_3 = num_1 + num_2 + memory
        s3 += str(num_3%10)
        memory = num_3//10
    if memory!=0:
        s3+=str(memory)
    return(s3[::-1])
Test = int(input())

while (Test!=0):
    Test -= 1;
    num_s = str(input())
    ok = False
    for i in range(0, 1001):
        num_check = int(num_s)
        if num_check%7 == 0:
            ok = True
            break
        num_s = sum_num(num_s)
    if (ok):
        print(num_s)
    else:
        print(-1)