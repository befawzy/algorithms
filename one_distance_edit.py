def isOneEditDistance(self, s: str, t: str) -> bool:
    """
    a function that checks if the two input strings are exactly one edit away.
    Edits that can be performed on strings are insert a character, remove a character or replace a character
    """
    count = 0
    if len(s) == len(t):
        for i in range(len(s)):
            if s[i] == t[i]:
                count += 1
    else:
        min_str = min(s, t)
        max_str = max(s, t)
        for letter in min_str:
            if letter in max_str:
                count += 1
                letter_index = max_str.index(letter)
                if len(max_str) > 0:
                    max_str = max_str[letter_index + 1 :]
                else:
                    break
    max_len = max(len(s), len(t))
    if count + 1 == max_len:
        return True
    else:
        return False
