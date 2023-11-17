for tc in range(int(input())):
    if tc != 4:
        # continue
        pass

    input()
    b = list(
        map(int, input().split())
    )

    minIndex = b.index(min(b))
    l1 = b[:minIndex + 1]
    l2 = b[minIndex + 1:]

    print(f'{l1=}; {l2=}')

    if len(l1) >= 2:
        for i in range(len(l1)):
            if i < len(l1) - 1:
                print(f'l1 Comparing: {i}, {i+1}')
                if l1[i+1] > l1[i]:
                    l1[i+1] = l1[i]
                    print('Making changes')

    if len(l2) >= 2:
        for i in range(len(l2)):
            if i < len(l2) - 1:
                print(f'l2 Comparing: {i}, {i+1}')
                if l2[i+1] < l2[i]:
                    l2[i] = l2[i+1]
                    print('Making changes')

    print(f'{l1=}; {l2=}')

    a = l1 + [0] + l2
    print(' '.join(map(str, a)))

    newB = [max(a[i], a[i+1]) for i in range(len(a) - 1)]
    print(newB)
    print(newB == b)
