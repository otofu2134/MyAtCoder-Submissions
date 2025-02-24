age, price = map(int, input().split())
if age>= 13:
    print(price)
elif age <= 5:
    print(0)
else:
    print(price // 2)