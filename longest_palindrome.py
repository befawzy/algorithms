def longestPalindrome(s: str) -> int:
    """Given a string s which consists of lowercase or uppercase letters,
     return the length of the longest palindrome that can be built with those letters.
     Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

     Input: s = "abccccdd"
     Output: 7 (One longest palindrome that can be built is "dccaccd", whose length is 7)
    A palindrome is a word that can be spelled backward or fawrawd
     Example: madam


    """
    if len(s) == 1:
        return 1
    count = 0
    there_is_odd_counts = False
    for i in set(s):
        if s.count(i) % 2 == 0:
            count += s.count(i)
        else:
            there_is_odd_counts = True
            count += s.count(i) - 1
    if there_is_odd_counts:
        count += 1
    return count
