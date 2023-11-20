input()

coins = sorted(map(int, input().split()), reverse=True)

half = sum(coins) // 2
coins_taken = 0
my_money = 0

for i in coins:
    coins_taken += 1
    my_money += i
    if my_money > half:
        break

print(coins_taken)
