# 1. Manual approach
# str1 = input()
# str2 = input()

# new_str = ''
# for i in range(len(str1)):
#     if str1[i] == '1' and str2[i] == '0':
#         new_str += '1'
#     elif str1[i] == '0' and str2[i] == '1':
#         new_str += '1'
#     else:
#         new_str += '0'

# print(new_str)

# 2. Approach using bitwise XOR
str1 = input()
str2 = input()

num1 = int(str1, 2)
num2 = int(str2, 2)

binary_string = bin(num1 ^ num2)[2:]
print(binary_string.rjust(len(str1), '0'))
