# I start with the first string as a prefix and compare it with the other strings.
# If characters match, I keep the prefix.
# If they differ, I shorten the prefix until it matches.
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        for i in range(len(strs[0])):
            char = strs[0][i]

            for word in strs:
                if i >= len(word) or word[i] != char:
                    return strs[0][:i]

        return strs[0]


strs = input("Enter words separated by space: ").split()

solution = Solution()

result = solution.longestCommonPrefix(strs)

print("Longest Common Prefix:", result)