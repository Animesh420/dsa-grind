# https://leetcode.com/problems/3sum/description/

'''
"""
3SUM — Two Pointers
Date: 2026-05-04 | Solved: Partial | Hints: Yes

WHAT I GOT RIGHT:
- Identified pivot approach: fix one number, apply two-sum on the rest
- Understood the core three-pointer structure

MISTAKES:
- Did not store values in final result list correctly
- Missed that sorting unlocks everything: duplicate skipping + early termination + two pointers
- Over-complicated with sets for uniqueness instead of inline duplicate skipping
- Missed duplicate skipping logic: if i > 0 and nums[i] == nums[i-1]: continue
- Missed early termination: if nums[i] > 0: break (no triplet possible if pivot is positive)

THE ONE RULE:
Sort first. Sorting gives you three wins for free:
duplicate skipping, early termination, and two-pointer — all from one operation.

PATTERN FINGERPRINT:
Sort + fix pivot + two pointers on remainder + skip duplicates at every level
'''

class Solution:
    
    def threeSum_slow(self, nums: list[int]) -> list[list[int]]:

        solutions = set()
        nums.sort()

        def two_sum(idx_to_ignore=-1, to_find=-1):
            h = dict()
            ans = []
            for i, val in enumerate(nums):
                if i == idx_to_ignore:
                    continue
                
                new_target = to_find - val

                if new_target in h:
                    ans.append([val, new_target])
                    continue

                if val not in h:
                    h[val] = i

            return ans

        def two_sum_2_ptr(start, to_find):
            ans = []
            i = start
            j = len(nums) - 1

            while i < j:
                s = nums[i] + nums[j]

                if s == to_find:
                    ans.append([nums[i], nums[j]])
                    i += 1
                    j -= 1
                elif s > to_find:
                    j -= 1
                elif s < to_find:
                    i += 1
            return ans 



        for i, val in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -val
            # result = two_sum(idx_to_ignore=i, to_find=target)
            result = two_sum_2_ptr(start=i+1, to_find=target)
   
            for option in result:
                res = [val, *option]
                solutions.add(tuple(res))

        return [list(x) for x in solutions]

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            # Optimization: If the smallest number > 0, sum can't be 0
            if nums[i] > 0:
                break
            
            # Skip duplicate fixed elements
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Inlined two_sum_2_ptr for speed
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # Skip duplicates for the left and right pointers
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res
        