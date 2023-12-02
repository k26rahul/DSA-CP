ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
word = input()

count_uppercase = 0
for letter in ascii_uppercase:
    count_uppercase += word.count(letter)

if count_uppercase > (len(word) - count_uppercase):
    print(word.upper())
else:
    print(word.lower())
