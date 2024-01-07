import time
from typing import List, Optional


class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        reversed_num = 0

        if x < 0:
            num = num * -1

        while num != 0:
            digit = num % 10
            reversed_num = reversed_num * 10 + digit
            num = num//10

        return reversed_num == x

    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(reverse=True)
        if len(strs) == 1:
            return strs[0]

        prefix = tuple([pre for pre in strs[0]])

        for word in strs[1::]:
            ans = ""
            if word.startswith(prefix):
                for idx, pre in enumerate(prefix):

                    if idx >= len(word):
                        print('true')
                        break

                    if word[idx] == pre:
                        ans += word[idx]
                    else:
                        break

            else:
                return ""

        return ans

    def isValid(self, s: str) -> bool:
        brackets = {"{": "}", "(": ")", "[": "]"}
        stack = []

        for bracket in s:
            if bracket in brackets:
                stack.append(bracket)
            # if first bracket is not an opening, it is wrong and wont be appended. Therefore, return false
            elif len(stack) == 0:
                return False
            # if the current bracket is not equals to the current value of the key-value pair in the dict, then its also wrong
            elif bracket != brackets[stack.pop()]:
                return False

        # lastly, we return if the stack has 0 len meaning all matches
        return len(stack) == 0

    def removeDuplicates(self, nums: List[int]) -> int:
        to_set = list(set(nums))
        nums.clear()
        for i in to_set:
            nums.append(i)
        nums.sort()
        return len(nums)

    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        haystack_len = len(haystack)

        for i in range(haystack_len - needle_len + 1):
            if haystack[i:i+needle_len] == needle:
                return i

        return -1

    def searchInsert(self, nums: List[int], target: int) -> int:
        # return the index of inserted target num

        for idx, i in enumerate(nums):
            if i == target:
                return idx

            elif i > target:
                return idx

        return len(nums)

    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str, digits))) + 1
        return [int(i) for i in str(num)]

    def isPalindrome2(self, s: str) -> bool:
        formatted = "".join([i for i in s if i.isalnum()]).lower()
        return formatted == formatted[::-1]

    def singleNumber(self, nums: List[int]) -> int:

        for i in nums:
            if nums.count(i) == 1:
                return i

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        total_len = len(flowerbed)
        flowers_left = n

        if flowers_left == 0:
            return True

        for i in range(total_len):
            if total_len == 1 and flowerbed[i] == 0 and flowers_left == 1:
                return True

            if total_len == 1 and flowerbed[i] == 1 and flowers_left == 1:
                return False

            if (i == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0) or (i == total_len - 1 and flowerbed[i] == 0 and flowerbed[i-1] == 0) or (flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                flowers_left -= 1

            if flowers_left == 0:
                return True
        return False

    def reverseVowels(self, s: str) -> str:
        # hello -> holle
        vowels = ['a', "e", 'i', 'o', 'u']
        to_list = [i for i in s]
        found_vowel_index = []
        popped_vowels = []

        for idx, i in enumerate(to_list):
            if i.lower() in vowels:
                found_vowel_index.append(idx)
                popped_vowels.append(to_list[idx])

        popped_vowels.reverse()

        for idx, i in enumerate(found_vowel_index):
            to_list[i] = popped_vowels[idx]

        return "".join(to_list)

    def reverseWords(self, s: str) -> str:
        to_list = s.split()

        return " ".join(to_list[::-1])


solution = Solution()
# print(solution.isPalindrome(-121))

# solution.longestCommonPrefix(["dog", "racecar", "car", "dogu", "do"])

# print(solution.isValid("{[]}"))

# solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])

# print(solution.strStr(haystack="sadbutsad2", needle="sad"))

# print(solution.searchInsert(nums=[1, 3, 5, 6], target=5))

# solution.lengthOfLastWord("   fly me   to   the moon  ")

# solution.plusOne(digits=[9])
# solution.plusOne(digits=[1, 2, 3, 4])

# print(solution.isPalindrome2("0P"))
# print(solution.isPalindrome2(s="race a car"))

# print(solution.singleNumber(nums=[4, 1, 2, 1, 2]))

# print(solution.canPlaceFlowers(
#     flowerbed=[1, 0, 0, 0, 0, 1], n=2))  # 1 flower

# print(solution.canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2))
# print(solution.canPlaceFlowers([0, 0, 1, 0, 0], 1))

# print(solution.reverseVowels(s="hello"))
# print(solution.reverseVowels(s="leetcode"))
# print(solution.reverseVowels(s="aA"))

# print(solution.reverseWords("  the sky is   blue "))
