# 1512. Number of Good Pairs
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j and nums[i] == nums[j]:
                    count += 1
        return count
                    
# 1051. Height Checker
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # expected = []
        # for i in range(len(heights)):
        #     expected.append(heights[i])


        # for i in range(len(expected)):
        #     for j in range(len(expected)-1):
        #         if expected[j] > expected[j+1]:
        #             expected[j],expected[j+1] = expected[j+1],expected[j]
        expected = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
    
        return count

# 977. Squares of a Sorted Array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            res.append(i**2)
        res.sort()
        return res

# 13. Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        ans = []
        for i in s:
            match i:
                case "I":
                    ans.append(1)
                case "V":
                    ans.append(5)
                case "X":
                    ans.append(10)
                case "L":
                    ans.append(50)
                case "C":
                    ans.append(100)
                case "D":
                    ans.append(500)
                case "M":
                    ans.append(1000)

        sum = 0
        for i in range(len(ans)-1):
            if ans[i] < ans[i+1]:
                sum -= ans[i]
            else:
                sum += ans[i]
        sum += ans[-1]
        return sum
    

    
