# https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1

def isPermutationPossible(booksArray, nosStudents, mid):
    allotment = 0
    nosStudentsAllocated = 1
    for numberOfPages in booksArray:
        if numberOfPages > mid:
            return False

        allotment += numberOfPages
        if allotment > mid:
            nosStudentsAllocated += 1
            if nosStudentsAllocated > nosStudents:
                return False
            allotment = numberOfPages

    return True


class Solution:
    def findPages(self, booksArray, nosBooks, nosStudents):
        if nosStudents > nosBooks:
            return -1

        low = max(booksArray)
        high = 10e6 * \
            (nosBooks if nosBooks == nosStudents else (nosBooks - nosStudents))
        while low <= high:
            mid = low + (high - low) // 2
            if isPermutationPossible(booksArray, nosStudents, mid):
                high = mid - 1
                answer = mid
            else:
                low = mid + 1

        return int(answer)


solution = Solution()
print(solution.findPages([12, 34, 67, 90], 4, 2))  # 113
print(solution.findPages([15, 17, 20], 4, 2))  # 32
