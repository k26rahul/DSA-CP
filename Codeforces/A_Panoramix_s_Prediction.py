n, m = map(int, input().split())


def check_prime(num):
    if num == 0 or num == 1:
        return False

    is_prime = True
    for i in range(2, int(num ** .5)+1):
        if num % i == 0:
            is_prime = False
            break
    return is_prime


# for i in range(50):
#     print(i, check_prime(i))

next_prime = None
for i in range(n + 1, m + 1):
    if check_prime(i):
        next_prime = i
        break

print('YES' if next_prime == m else 'NO')
