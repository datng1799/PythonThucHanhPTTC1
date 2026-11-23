import math as mth
Test = int(input())

def check_prime(n):
    if n<2:
        return False
    i = 2;
    while i*i<=n:
        if (n%i==0):
            return False
        i+=1
    return True

def cal_element(n):
    sum = 0
    while (n!=0):
        sum += n%10
        n//=10
    return sum

while (Test!=0):
    Test -= 1
    num_1, num_2 = map(int, input().split())
    _gcd = mth.gcd(num_1, num_2)
    if check_prime(cal_element(_gcd)):
        print("YES")
    else:
        print("NO")
