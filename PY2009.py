Test = int(input())

while (Test != 0):
    Test -= 1
    s_code = str(input())
    buf = []
    res = ""
    current_s = ""
    i = len(s_code)-1
    while (i!=-1):
        if s_code[i] == ']':
            buf.append("")
            i -=1
        elif s_code[i] == '[':
            current_s = buf[-1]
            buf.pop(-1)
            i-=1
        elif '0'<=s_code[i]<='9':
            num_s = ""
            while '0'<=s_code[i]<='9' and i>-1:
                num_s = str(s_code[i])+num_s
                i -=1
            num = int(num_s)
            current_s="".join(current_s*num)
            if len(buf)==0:
                res+=current_s
                current_s =""
            else:
                buf[-1]+=current_s
                current_s = ""
        else:
            if len(buf)>0:
                buf[-1]+=str(s_code[i])
            else:
                res+=str(s_code[i])
            i -=1
    print(res[::-1])