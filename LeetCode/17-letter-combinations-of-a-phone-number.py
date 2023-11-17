# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

'''
Create a dictionary called mapping that maps each digit from 2 to 9 to a list of corresponding letters

Define a function called letterCombinations that takes a string called digits as input
    If the length of digits is 0, return an empty list

    Create an empty list called digitsArr
    For each digit in digits:
        Append the corresponding list of letters from the mapping dictionary to digitsArr

    While the length of digitsArr is greater than 1:
        Create a list called s that contains the last two elements of digitsArr
        Remove the last two elements of digitsArr and replace them with an empty list
        For each letter i in the first element of s:
            For each letter j in the second element of s:
                Append the string i + j to the last element of digitsArr

    Return the first element of digitsArr
'''

mapping = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}


class Solution:
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []

        digitsArr = []
        for digit in digits:
            digitsArr.append(mapping[digit])

        while len(digitsArr) > 1:
            s = digitsArr[-2:]
            digitsArr = digitsArr[:-2]
            digitsArr.append([])
            for i in s[0]:
                for j in s[1]:
                    digitsArr[-1].append(i + j)

        return digitsArr[0]


print(Solution().letterCombinations('23'))
print(Solution().letterCombinations(''))
print(Solution().letterCombinations('2'))
