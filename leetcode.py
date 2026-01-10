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
    
# 43. Multiply Strings
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num3 = int(num1)
        num4 = int(num2)
        ans = str(num3 * num4)
        return ans

# 349. Intersection of Two Arrays
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i] == nums2[j]:
        #             if nums1[i] not in ans:
        #                 ans.append(nums1[i])
        # return ans
        nums3 = set(nums1)
        nums4 = set(nums2)
        for i in nums3:
            if i in nums4:
                ans.append(i)
        return ans

# 1678. Goal Parser Interpretation
class Solution:
    def interpret(self, command: str) -> str:
        # ans = list(command)
        # for i in range(len(ans)):
        #     if ans[i] == "G":
        #         ans[i] = "G"
        #     elif ans[i] == "()":
        #         ans[i] = "o"
        #     elif ans[i] == "(al)":
        #         ans[i] = "al"
        # return str(ans)
        command = command.replace("()","o")
        command = command.replace("(al)","al")
        return command


# 27. Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count+=1
        return count 

# 58. Length of Last Word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        for i in s:
            return len(s[-1])

# 35. Search Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)

# 217. Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        #         break
        # return False
        arr = set(nums)
        if len(nums) != len(arr):
            return True
        else:
            return False

# 242. Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # for i in s:
        #     if i not in t:
        #         return False
        #     else:
        #         t = t.replace(i,"",1)
        # return True
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        return s==t
    
