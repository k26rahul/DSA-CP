from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        k = []
        for i in range(1, n + 1):
            el = i
            if i % 3 == 0:
                el = 'Fizz'
            if i % 5 == 0:
                el = 'Buzz'
            if i % 3 == 0 and i % 5 == 0:
                el = 'FizzBuzz'
            k.append(str(el))
        return k


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        k = []
        for i in range(1, n + 1):
            el = i
            divisibleBy3 = i % 3 == 0
            divisibleBy5 = i % 5 == 0
            if divisibleBy3 and divisibleBy5:
                el = 'FizzBuzz'
            elif divisibleBy3:
                el = 'Fizz'
            elif divisibleBy5:
                el = 'Buzz'
            k.append(str(el))
        return k


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        k = []
        for i in range(1, n + 1):
            el = ''
            divisibleBy3 = i % 3 == 0
            divisibleBy5 = i % 5 == 0

            if divisibleBy3:
                el += 'Fizz'
            if divisibleBy5:
                el += 'Buzz'
            if len(el) == 0:
                el = str(i)

            k.append(el)
        return k


print(Solution().fizzBuzz(5))
