T = int(input())

for _ in range(T):
  word1, word2 = input().split()
  print(f'{word2[0] + word1[1:]} {word1[0] + word2[1:]}')
