# https://practice.geeksforgeeks.org/problems/1a31d09f7b8e9c0633339df07858deb3a728fe19/1

from itertools import accumulate


def farNumber(N, Arr):
    sorted_arr = sorted([(Arr[i], i)
                        for i in range(N)], key=lambda tup: tup[0])

    cumulative_max_arr = list(
        accumulate([tup[1] for tup in sorted_arr], max)
    )

    final_sorted = sorted(
        list(zip(sorted_arr, cumulative_max_arr)), key=lambda tup: tup[0][1]
    )

    print('Arr:', Arr)
    print('sorted_arr:', sorted_arr)
    print('cumulative_max_arr:', cumulative_max_arr)
    print('final_sorted:', final_sorted)

    return [cumulative_max if cumulative_max > index else - 1
            for ((num, index), cumulative_max) in final_sorted]


print(farNumber(5, [3, 1, 5, 2, 4]))
