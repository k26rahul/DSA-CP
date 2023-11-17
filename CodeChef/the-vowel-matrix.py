# https://www.codechef.com/problems/VOWMTRX?tab=statement

def sol(input1, givenString):
    # Your solution code here
    k = int(input1.split(' ')[1])

    vowelsInCurrentSubstr = 0
    isBeyondSubstr = False
    stepsBeyondSubstr = 0
    stepper = 1

    for char in givenString:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            if isBeyondSubstr:
                isBeyondSubstr = False
                stepper *= (stepsBeyondSubstr + 1)
                stepsBeyondSubstr = 0

            vowelsInCurrentSubstr += 1
            if vowelsInCurrentSubstr == k:
                vowelsInCurrentSubstr = 0
                isBeyondSubstr = True

        elif isBeyondSubstr:
            stepsBeyondSubstr += 1

    print(stepper % (10**9 + 7))


# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read the inputs for each test case
    input1 = input().strip()
    input2 = input().strip()

    # Call the solution function
    sol(input1, input2)
