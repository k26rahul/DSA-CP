from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(k) for k in accounts)


print(Solution().maximumWealth([[1, 2, 3], [3, 2, 1]]))
