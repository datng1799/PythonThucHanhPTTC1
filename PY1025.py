num1, num2 = map(int, input().split())

if (num1*num2<=0 or num1+num2<=0):
    print('0')
else:
    print(f"{2*(num1+num2)} {num1*num2}")