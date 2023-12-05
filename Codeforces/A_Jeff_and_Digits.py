n = int(input())
nums = input().split()

c0 = nums.count('0')
c5 = nums.count('5')

if c0 == 0:
    print(-1)
elif c5 < 9:
    print(0)
else:
    print('555555555' * int(5 * c5 / 45) + '0' * c0)
