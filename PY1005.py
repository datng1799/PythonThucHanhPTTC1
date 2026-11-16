from subprocess import check_output

count_4 = 0
count_7 = 0

num_input = str(input())

for i in range(0, len(num_input)):
    if (num_input[i] == '4'):
        count_4 +=1
    elif (num_input[i] == '7'):
        count_7 +=1
if ((count_7 + count_4 == 4) or (count_7 + count_4 == 7)):
    print("YES")
else: print("NO")
