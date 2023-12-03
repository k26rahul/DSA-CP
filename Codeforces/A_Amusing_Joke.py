ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

guest_host = input() + input()
pile = input()

found = True
for letter in ascii_uppercase:
    if guest_host.count(letter) != pile.count(letter):
        found = False

print('YES' if found else 'NO')
