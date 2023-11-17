# https://leetcode.com/problems/combination-sum-iii/description/

'''
Define a function called combinations that takes two arguments, an array called arr and an integer called k
    If k equals 0, return a list containing an empty list
    If the length of arr is less than k, return an empty list

    Create an empty list called result
    For each index i in the range from 0 to the length of arr minus 1:
        Set first to be a list containing the i-th element of arr
        Set rest to be the result of calling combinations recursively with the slice of arr starting from i+1 and k-1 as arguments
        For each item in rest:
            Append the concatenation of first and item to result

    Return result
'''


def combinations(arr, k):
    if k == 0:
        return [[]]
    if len(arr) < k:
        return []

    result = []
    for i in range(len(arr)):
        first = arr[i:i+1]
        rest = combinations(arr[i+1:], k-1)
        for item in rest:
            result.append(first + item)
    return result


class Solution:
    def combinationSum3(self, k, n): pass
