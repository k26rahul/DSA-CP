# https://www.spoj.com/problems/HC/

from colorama import Fore, Style


def color(text, color=Fore.GREEN):
    return color + str(text) + Style.RESET_ALL


coins = 'HHLLH'

n = len(coins)
print(f'L = {coins.count("L")}, H = {coins.count("H")}')
print('Game Begins 🚩', '\n')

finalCoinBelongsTo = None
for i in range(n):
    if i == n - 1:
        finalCoinBelongsTo = coins
        break

    if i % 2 == 0:  # L's chance
        if 'LH' in coins:
            j = coins.index('LH')
            print(f"L round {i}".ljust(12),
                  f'{coins[:j]}{color(coins[j:j+2])}{coins[j+2:]}', coins.count('L'), coins.count('H'))

            coins = coins.replace('LH', 'L', 1)

            print(f''.ljust(12),
                  f'{coins[:j]}{color("L")}.{coins[j+1:]}')

        elif 'HL' in coins:
            j = coins.index('HL')
            print(f"L round {i}".ljust(12),
                  f'{coins[:j]}{color(coins[j:j+2])}{coins[j+2:]}', coins.count('L'), coins.count('H'))

            coins = coins.replace('HL', 'L', 1)

            print(f''.ljust(12),
                  f'{coins[:j]}{color("L")}.{coins[j+1:]}')

        elif 'LL' in coins:
            j = coins.index('LL')
            print(f"L round {i}".ljust(12),
                  f'{coins[:j]}{color(coins[j:j+2])}{coins[j+2:]}', coins.count('L'), coins.count('H'))

            coins = coins.replace('LL', 'H', 1)

            print(f''.ljust(12),
                  f'{coins[:j]}{color("H")}.{coins[j+1:]}')

        elif 'HH' in coins:
            j = coins.index('HH')
            print(f"L round {i}".ljust(12),
                  f'{coins[:j]}{color(coins[j:j+2])}{coins[j+2:]}', coins.count('L'), coins.count('H'))

            coins = coins.replace('HH', 'H', 1)

            print(f''.ljust(12),
                  f'{coins[:j]}{color("H")}.{coins[j+1:]}')

    else:  # H's chance
        if 'LL' in coins:
            j = coins.index('LL')
            print(f"H round {i}".ljust(12),
                  f'{coins[:j]}{color(coins[j:j+2], Fore.RED)}{coins[j+2:]}', coins.count('L'), coins.count('H'))

            coins = coins.replace('LL', 'H', 1)

            print(f''.ljust(12),
                  f'{coins[:j]}{color("H", Fore.RED)}.{coins[j+1:]}')

        elif 'HH' in coins:
            j = coins.index('HH')
            print(f"H round {i}".ljust(12),
                  f'{coins[:j]}{color(coins[j:j+2], Fore.RED)}{coins[j+2:]}', coins.count('L'), coins.count('H'))

            coins = coins.replace('HH', 'H', 1)

            print(f''.ljust(12),
                  f'{coins[:j]}{color("H", Fore.RED)}.{coins[j+1:]}')

        elif 'LH' in coins:
            j = coins.index('LH')
            print(f"H round {i}".ljust(12),
                  f'{coins[:j]}{color(coins[j:j+2], Fore.RED)}{coins[j+2:]}', coins.count('L'), coins.count('H'))

            coins = coins.replace('LH', 'L', 1)

            print(f''.ljust(12),
                  f'{coins[:j]}{color("L", Fore.RED)}.{coins[j+1:]}')

        elif 'HL' in coins:
            j = coins.index('HL')
            print(f"H round {i}".ljust(12),
                  f'{coins[:j]}{color(coins[j:j+2], Fore.RED)}{coins[j+2:]}', coins.count('L'), coins.count('H'))

            coins = coins.replace('HL', 'L', 1)

            print(f''.ljust(12),
                  f'{coins[:j]}{color("L", Fore.RED)}.{coins[j+1:]}')


print('\nGame Ends 🚩\n')
print(f'{color("finalCoinBelongsTo:", Fore.CYAN)}', finalCoinBelongsTo)
