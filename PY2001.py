my_set  = set()

N = int(input())

for i in range(0,N):
    a = int(input())
    my_set.add(a)

my_list = list(my_set)

my_list.sort()

for i in range(0, len(my_list)):
    print(my_list[i], end=" ")