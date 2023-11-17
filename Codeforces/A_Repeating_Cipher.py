# https://codeforces.com/problemset/problem/1095/A

n = int(input())
inputStr = input()


outputStr = ''
ptr = 0
i = 0
while True:
    ptr += i
    if ptr > n - 1:
        break
    outputStr += inputStr[ptr]
    i += 1

print(outputStr)
