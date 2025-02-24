price = int(input())
a = int(input())
b = price // 500
rest = price - 500* b
if price % 500 ==0:
    print("Yes")
else:
    if rest <= a:
        print("Yes")
    else:
        print("No")