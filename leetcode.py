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

# 