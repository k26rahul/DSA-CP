# https://codeforces.com/contest/1846/problem/C

import sys

for q in range(int(sys.stdin.readline())):
    n, m, h = [int(x) for x in sys.stdin.readline().split(' ')]

    rudolfPoints, rudolfPenalty = 0, 0
    rudolfPlace = 1

    for i in range(n):
        m = sorted([int(x) for x in sys.stdin.readline().split(' ')])
        time, points, penalty = 0, 0, 0

        for minutes in m:
            time += minutes
            if time > h:
                break
            points += 1
            penalty += time

        if i == 0:
            rudolfPoints, rudolfPenalty = points, penalty
        elif points > rudolfPoints:
            rudolfPlace += 1
        elif points == rudolfPoints and penalty < rudolfPenalty:
            rudolfPlace += 1

    print(rudolfPlace)
