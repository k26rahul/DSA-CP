n = int(input())
pages_a_day = list(map(int, input().split()))

day = 0
done = 0
while done < n:
    if day == 7:
        day = 0
    done += pages_a_day[day]
    # print(day, done)
    day += 1


print(day)
