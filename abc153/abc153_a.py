hp , attack = map(int , input().split())
count = hp / attack
i = 0
for counts in range(int(count) + 1) :
    if hp > 0:
      hp -= attack
      i += 1
    else:
      break
print(i)