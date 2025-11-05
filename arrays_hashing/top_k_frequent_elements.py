'''
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique
'''
from collections import Counter

def topKFrequent(nums, k):  # O(nlogn)
    d = {}
    for x in nums:
        d[x] = d.get(x, 0) + 1

    ans = sorted(d, key=lambda x: -d[x])
    return ans[0:k]

def topKFrequent2(nums, k): #O(n)
    d = {}
    freq = [[] for i in range(len(nums)+1)]
    print(freq)
    for x in nums:
        d[x] = d.get(x, 0) + 1

    for key, value in d.items():
        freq[value].append(key)

    ans = []
    for i in range(len(freq)-1, 0, -1):
        if len(freq[i]) > 0:
            for x in freq[i]:
                ans.append(x)
                if len(ans) == k: return ans
    return ans

if __name__ == '__main__':
    nums = [5,1,3,1,3,2,2,1,2,1,2]
    k = 2
    print(topKFrequent2(nums, k))