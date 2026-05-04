# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

"""
TWO SUM II — Two Pointers
Date: 2026-05-04 | Solved: Partial | Hints: Yes

WHAT I GOT RIGHT:
- Got the answer using sorting approach
- Understood the two-pointer direction logic

MISTAKES:
- Assumed array was not sorted — did not re-read the constraint that it IS already sorted
- Went for sorting + two pointers which broke 1-indexed output requirement
- Missed that a pre-sorted array means two pointers work directly, no hashmap needed

THE ONE RULE:
Always check if the array is already sorted — if yes, two pointers work in O(n)
with no extra space. Sorting an already-sorted array to "be safe" breaks index guarantees.

PATTERN FINGERPRINT:
Pre-sorted + two pointers inward + adjust based on sum vs target
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums=numbers
        n=len(numbers)

        l,r=0,n-1
        while l<r:
            if nums[l]+nums[r]==target:
                return [l+1,r+1]
            elif nums[l]+nums[r]<target:
                l+=1
            else: r-=1
        
        