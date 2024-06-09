# https://codeforces.com/contest/1979/problem/A

"""
Problem:
Bob selects two indices and finds the maximum value in the subarray between these indices.
Alice wins if this maximum is greater than k.

Strategy:
1. For each test case, find the minimum value of the maximums from all 
   adjacent pairs in the array.
2. Alice wins if k is less than this minimum maximum, so we output 
   (minimum maximum - 1).
"""

"""
Explanation of the Code
1. Input Reading:
   - The first line reads the number of test cases, T.
   - For each test case, the number of elements in the array n is read.
   - The array elements are read and stored in the list array.

2. Finding Minimum of Adjacent Maximums:
   - Initialize min_maxx to infinity to find the smallest maximum of any two 
     adjacent elements in the array.
   - Loop through the array from the start to the second last element 
     (index n-2), because we are considering pairs of adjacent elements.
   - For each element array[i], find the maximum value between array[i] and 
     array[i+1].
   - Update min_maxx if this maximum is smaller than the current min_maxx.

3. Output Calculation:
   - The maximum integer k at which Alice is guaranteed to win is min_maxx - 1.
   - Print this value for each test case.

Example:
- For the array [2, 4, 1, 7], the adjacent pairs are (2, 4), (4, 1), and (1, 7). 
  The maximums of these pairs are 4, 4, and 7 respectively. The smallest of 
  these maximums is 4, so Alice can guarantee a win if k is 3 or less.
"""

# Read the number of test cases
T = int(input())

# Loop over each test case
for _ in range(T):
  # Read the number of elements in the array
  n = int(input())
  # Read the elements of the array
  array = list(map(int, input().split()))

  # Initialize the minimum of all adjacent maximums to infinity
  min_maxx = float('inf')

  # Loop through each element to find the maximums of adjacent pairs
  for i in range(n - 1):  # We go up to n-1 to avoid out of bounds
    # Find the maximum of the current element and the next element
    maxx = max(array[i], array[i + 1])

    # Update the minimum of these maximums
    if maxx < min_maxx:
      min_maxx = maxx

  # Alice is guaranteed to win if k is less than the minimum maximum found
  print(min_maxx - 1)
