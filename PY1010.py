Test = int(input())

while (Test!=0):
    Test -= 1
    string_inp = str(input())
    leng = len(string_inp)
    if (string_inp[0]==string_inp[leng-2] and string_inp[1]==string_inp[leng-1]):
        print("YES")
    else:
        print("NO")