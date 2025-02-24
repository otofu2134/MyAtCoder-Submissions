money = int(input())
price_a = int(input())
price_b = int(input())
money_after_buying_a = money - price_a
count = money_after_buying_a // price_b
print(money_after_buying_a - price_b * count)