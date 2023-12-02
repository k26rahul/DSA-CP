number = input()

count_lucky_digits = str(number.count('4') + number.count('7'))

is_nearly_lucky = count_lucky_digits.count(
    '4') + count_lucky_digits.count('7') == len(count_lucky_digits)

print('YES' if is_nearly_lucky else 'NO')
