import math

T = int(input())


for _ in range(T):
    N, H = map(int, input().split())
    durations = sorted(map(int, input().split()), reverse=True)

    print(H, durations)
    durations = [duration + 1 for duration in durations]
    print(H, durations)

    print('STEPS')
    spent = 0
    least_duration = durations[-1] - 1
    for index, duration in enumerate(durations):
        spent += duration
        margin = H - spent
        margin_split_max = math.ceil(margin / (2 + index))

        print(spent, margin_split_max, least_duration)

        if (margin_split_max < least_duration):
            print('VOILA -->', index + 1)
            break
