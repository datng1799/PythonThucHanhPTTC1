Test = int(input())

while (Test != 0):
    Test -=1
    count = 0
    num_s = str(input())
    num_list = list(int(i) for i in num_s.split())
    num_list.sort()
    for i in range(0, len(num_list)-2):
        for j in range(i+1, len(num_list)-1):
            for k in range(j+1, len(num_list)):
               if num_list[k]<(num_list[j]+num_list[i]):
                  count +=1
    print(count)