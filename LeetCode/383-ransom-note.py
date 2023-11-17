from typing import List

lowercase_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                  'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not any(
            ransomNote.count(letter) > magazine.count(letter) for letter in lowercase_list
        )


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        x = {letter: magazine.count(letter) for letter in lowercase_list}
        y = {letter: ransomNote.count(letter) for letter in lowercase_list}

        for letter in lowercase_list:
            if y[letter] > x[letter]:
                return False

        return True


print(Solution().canConstruct('aa', 'aab'))
