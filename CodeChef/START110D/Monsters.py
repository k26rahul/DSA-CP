import math


def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for number in range(2, int(limit**0.5) + 1):
        if is_prime[number]:
            for multiple in range(number * number, limit + 1, number):
                is_prime[multiple] = False

    primes = [num for num in range(2, limit + 1) if is_prime[num]]
    return primes


T = int(input())


def generate_prefix_sum(series):
    prefix_sum = []
    current_sum = 0

    for num in series:
        current_sum += num
        prefix_sum.append(current_sum)

    return prefix_sum


# Given series
input_series = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024,
                2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]

# Generate the prefix sum
result_prefix_sum = generate_prefix_sum(input_series)
print(result_prefix_sum)


regular = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048,
           4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]
special = sieve_of_eratosthenes(1000000)

mapping = {key: -1 for key in range(1, 1000000)}


for s in special:
    mapping[s] = 1
    for r in regular:
        if (mapping[s + r]):
            pass

print(mapping)

for _ in range(T):
    H = int(input())
    pass
