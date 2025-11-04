'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
'''

from collections import Counter

def isAnagram(s, t):
    s = sorted(s)
    t = sorted(t)
    return s == t

def isAnagram2(s, t):
    ds = {}
    dt = {}

    for x in s:
        ds[x] = ds.get(x, 0) + 1

    for x in t:
        dt[x] = dt.get(x, 0) + 1

    return ds == dt

def isAnagram3(s, t):
    return Counter(s) == Counter(t)

def isAnagram4(s, t):
    if len(s) != len(t): return False
    for i in set(s):
        if s.count(i) != t.count(i):
            return False
    return True

if __name__ == '__main__':
    s = input()
    t = input()
    if isAnagram3(s, t):
        print('true')
    else:
        print('false')