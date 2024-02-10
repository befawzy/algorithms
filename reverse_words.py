from typing import List


def reverseWords(s: List[str]) -> None:
    """
    Given a character array s, reverse the order of the words. A word is defined as a sequence of non-space characters.
    The words in s will be separated by a single space. Your code must solve the problem in-place,
    i.e. without allocating extra space.
    Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
    """
    s.reverse()
    start = 0
    for i in range(len(s)):
        if s[i] == " ":
            s[start:i] = s[start:i][::-1]
            start = i + 1
        if i == len(s) - 1:
            s[start:] = s[start:][::-1]


# s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
s = [" "]

reverseWords(s)

print(s)
