import math as mth

def cal_phi(n):
    res = 0
    for i in range(1,n):
        if mth.gcd(i, n) == 1:
            res += 1
    return res

def check_prime(n):
    if (n<2):
        return False
    i = 2
    while i*i<=n:
        if n%i == 0:
            return False
        i += 1
    return True


Test = int(input())

while (Test!=0):
    Test -=1
    check_num = int(input())
    if check_prime(cal_phi(check_num)):
        print("YES")
    else:
        print("NO")