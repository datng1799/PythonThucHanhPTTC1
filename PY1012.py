num_a, num_K, num_N = map(int, input().split())

list = []

i = (num_a//num_K)*num_K

while (i<=num_N):
    num_b = i - num_a;
    if num_b>0:
        list.append(num_b)
    i+=num_K

if len(list) == 0:
    print(-1)
else:
    for i in range (0, len(list)):
        print(list[i], end=" ")