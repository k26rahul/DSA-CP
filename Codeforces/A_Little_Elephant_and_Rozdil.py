n = int(input())
cities = list(map(int, input().split()))

mini = min(cities)
if cities.count(mini) == 1:
    print(cities.index(mini) + 1)
else:
    print('Still Rozdil')
