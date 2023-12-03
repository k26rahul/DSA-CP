n = int(input())
passengers = []

for i in range(n):
    passengers.append(list(map(int, input().split())))

minimum_capacity = 0
capacity = 0
for exit, enter in passengers:
    capacity -= exit
    capacity += enter
    if capacity > minimum_capacity:
        minimum_capacity = capacity
    # print(exit, enter)

print(minimum_capacity)
