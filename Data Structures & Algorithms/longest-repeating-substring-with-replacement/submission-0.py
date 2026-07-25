class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_frq = {}
        max_frq = 0
        max_len = 0
        left = 0

        for right in range(len(s)):
            char_frq[s[right]] = char_frq.get(s[right],0) + 1

            max_frq = max(max_frq, char_frq[s[right]])

            if ((right - left + 1) - max_frq) > k:
                char_frq[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

        