fib = [0, 1]
for i in range(2, 50):
    fib.append(fib[i - 2] + fib[i - 1])

n = int(input())

if n == 0:
    print('0 0 0')
elif n == 1:
    print('0 0 1')
elif n == 2:
    print('0 1 1')
else:
    i = fib.index(n)
    print(f'{fib[i - 1]} {fib[i - 3]} {fib[i - 4]}')
