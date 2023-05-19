# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

def lengthOfLongestSubstring(input_string):
    """
    :type input_string: str
    :rtype: int
    """
    seen = {}
    lgt = 0
    length = 0
    for i in range(len(input_string)):            
        char = input_string[i]
        if char in seen and seen[char] >= lgt:
            lgt = seen[char] + 1
        else:
            length = max(length, i - lgt + 1)
        seen[char] = i

    return length


input_string = "abcabcbb"
print(lengthOfLongestSubstring(input_string))
