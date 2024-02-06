def isSubsequence(s: str, t: str) -> bool:
    """
    given strings s and t, return true if s is a substring of t. False otherwise.
    Example 1:

    Input: s = "abc", t = "ahbgdc"
    Output: true

    Example 2:

    Input: s = "axc", t = "ahbgdc"
    Output: false
    """
    sliced_len = 0
    count = 0
    for i in s:
        if len(t) > 0 and (i in t):
            letter_index = t.index(i)
            count += 1
            sliced_len += len(t) - len(t[letter_index + 1 :])
            t = t[letter_index + 1 :]
        else:
            return False
    if count == len(s):
        return True
    else:
        return False


s = "bb"
t = "ahbgdc"


isSubsequence(s, t)  # False
