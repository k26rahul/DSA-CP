def permutations(string):
    if len(string) == 0:
        return []
    elif len(string) == 1:
        return [string]

    perms = []

    for i in range(len(string)):
        char = string[i]
        remaining_chars = string[:i] + string[i + 1:]
        sub_perms = permutations(remaining_chars)

        for perm in sub_perms:
            perms.append(char + perm)

    return perms


for perm in permutations('abc'):
    print(perm)
