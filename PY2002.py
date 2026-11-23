Test = int(input())

while (Test !=0):
    Test -= 1
    num_s = str(input())
    k = int(input())
    res =""
    my_list = list()
    for e in num_s.split():
        my_list.append(int(e))

    count = 0
    for i in range(0, len(my_list)-1):
        for j in range(i+1, len(my_list)):
            if my_list[i]+my_list[j] == k:
                res += f"({my_list[i]}, {my_list[j]}) "
                count+=1
    res.rstrip()
    if count == 0:
        print("NO")
    else:
        print(res)