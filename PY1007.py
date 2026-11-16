Test = int(input())

while (Test!=0):
    Test -=1
    money_funds, money_interest, money_funds_wish = map(float, input().split())
    years = int(0)
    while (money_funds<money_funds_wish):
        money_funds = money_funds* float((100+money_interest)/100)
        years +=1
    print(years)