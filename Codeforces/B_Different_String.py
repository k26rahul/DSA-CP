T = int(input())

for _ in range(T):
  word = input()
  letters = list(word)
  unique_letters = list(set(letters))

  if len(unique_letters) == 1:
    print('NO')
  else:
    print('YES')
    unique_letter1 = unique_letters[0]
    unique_letter2 = unique_letters[1]

    index_unique_letter1 = letters.index(unique_letter1)
    index_unique_letter2 = letters.index(unique_letter2)

    letters[index_unique_letter1], letters[index_unique_letter2] = \
        letters[index_unique_letter2], letters[index_unique_letter1]

    print(''.join(letters))


"""
d -> NO
aa -> NO
zzzzz -> NO

Otherwise YES
ap1p2le (apple) -> ap2p1le (apple) -> Fail
apple -> appel, eappl, lappe -> Pass
LOGIC: paple -> a,p,l,e

add
dad

rahul -> arhul Pass
ooc -> ooc Fail
"""
