# https://codeforces.com/problemset/problem/371/C

recipe = input()
n_bread, n_sausage, n_cheese = [int(x) for x in input().split(' ')]
p_bread, p_sausage, p_cheese = [int(x) for x in input().split(' ')]
rubles = int(input())

r_bread = recipe.count('B')
r_sausage = recipe.count('S')
r_cheese = recipe.count('C')

nosHamburgers = min([
    float('inf') if r_bread == 0 else n_bread // r_bread,
    float('inf') if r_sausage == 0 else n_sausage // r_sausage,
    float('inf') if r_cheese == 0 else n_cheese // r_cheese,
])

print(nosHamburgers)

rubles += sum(
    [
        (n_bread - (r_bread * nosHamburgers)) * p_bread,
        (n_sausage - (r_sausage * nosHamburgers)) * p_sausage,
        (n_cheese - (r_cheese * nosHamburgers)) * p_cheese,
    ]
)

print(nosHamburgers + rubles // (p_bread * r_bread +
      p_sausage * r_sausage + p_cheese * r_cheese))
