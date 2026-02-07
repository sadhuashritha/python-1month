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
    
# 49. Group Anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]
        ans = {}
        for i in range(len(strs)):
            res = ''.join(sorted(strs[i]))
            if res in ans:
                ans[res].append(strs[i])
            else:
                ans[res] = [strs[i]]

        return list(ans.values())

    
# 169. Majority Element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]]+=1
        
        # return max(d, key=d.get)
        n = len(nums)
        for key,value in d.items():
            if value > (n/2):
                return key
            

# 121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum = 0
        min = prices[0]
        for i in range(len(prices)):
            n = prices[i] - min
            if n > sum:
                sum = n
            if prices[i] < min:
                min = prices[i]
        return sum


#  1281. Subtract the Product and Sum of Digits of an Integer
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n1 = str(n)
        p = 1
        s = 0
        for i in range(len(n1)):
            p *= int(n1[i])
            s += int(n1[i])
        ans = p - s
        return ans 

# 347. Top K Frequent Elements
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        ans = sorted(freq,key = freq.get, reverse = True)
        return ans[:k]

# 1207. Unique Number of Occurrences
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in range(len(arr)):
            if arr[i] in d:
                d[arr[i]] +=1
            else:
                d[arr[i]] = 1

        values = d.values()
        if len(values) == len(set(values)):
            return True
        else:
            return False
        
# 152. Maximum Product Subarray
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(len(nums)):
            mul = 1
            for j in range(i,len(nums)):
                mul *= nums[j]
                if ans < mul:
                    ans = mul
        return ans

# 2283. Check if Number Has Equal Digit Count and Digit Valueclass Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(len(num)):
            if int(num[i]) != num.count(str(i)):
                return False
        return True

# 1374. Generate a String With Characters That Have Odd Counts

class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 != 0:
            return "a" * n
        else:
            return "a" * (n-1) + "b"

# 434. Number of Segments in a String
class Solution:
    def countSegments(self, s: str) -> int:
        s1 = s.split()
        # return len(s1)
        count = 0
        for i in range(len(s1)):
            count += 1
        return count
    
# 657. Robot Return to Origin
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # x = 0
        # y = 0
        # for i in moves:
        #     if i == "U":
        #         y += 1
        #     elif i == "D":
        #         y -= 1
        #     elif i == "L":
        #         x -= 1
        #     else:
        #         x += 1
        # return  x == 0 and y == 0
        for i in moves:
            left = moves.count("L")
            right = moves.count("R")
            up = moves.count("U")
            down = moves.count("D")

            if left == right and up == down:
                return True
            else:
                return False
            
# 26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = []
        for i in range(len(nums)):
            if nums[i] not in res:
                res.append(nums[i])

        for i in range(len(res)):
            nums[i] = res[i]
        return len(res)
        
# 2824. Count Pairs Whose Sum is Less than Target
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] < target :
                    count += 1      
        return count

# 66. Plus One
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result  = "".join(map(str,digits)) # result = 123 --> string
        result = int(result) + 1 # result -> int + 1
        ans = list(map(int,str(result))) # result -> map(int, "1234")
        return ans

    
# 11. Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height) - 1
        maxarea = 0
        while p1 < p2:
            mini = min(height[p1],height[p2])
            area = mini * (p2 - p1)
            maxarea = max(maxarea,area)
            if(height[p1]<height[p2]):
                p1+=1
            else:
                p2 -=1
        return maxarea

# 283. Move Zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[p1] = nums[p1],nums[i]
                p1 += 1


# 167. Two Sum II - Input Array Is Sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            s = numbers[left] + numbers[right] 
            if s == target and left != right:
                return (left +1,right+1)
            elif s < target:
                left += 1
            else:
                right -= 1


