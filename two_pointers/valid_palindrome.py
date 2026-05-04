# https://leetcode.com/problems/valid-palindrome/

"""
VALID PALINDROME — Two Pointers
Date: 2026-05-04 | Solved: Partial | Hints: Yes

WHAT I GOT RIGHT:
- Correctly identified two-pointer logic: start and end moving inward

MISTAKES:
- Didn't read full problem: missed alphanumeric filter requirement
  Rule: Read constraints before writing logic — they ARE the problem

THE ONE RULE:
Read the full problem statement first. Always.

PATTERN FINGERPRINT:
Two pointers + skip non-valid chars + compare inward
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:

        i = 0
        j = len(s) - 1

        while i < j:
            if not s[i].isalnum():
                i += 1

            elif not s[j].isalnum():
                j -= 1

            elif s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1

        return True

