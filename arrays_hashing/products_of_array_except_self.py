'''
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in
O(n)
O(n) time without using the division operation?

Example 1:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]

Example 2:
Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]

Constraints:
2 <= nums.length <= 1000
-20 <= nums[i] <= 20

'''

def productExceptSelf(nums):
    res = 1
    for x in nums:
        if x != 0: res *= x

    cnt = nums.count(0)
    ans = []
    for x in nums:
        if x != 0:
            if cnt == 0:
                ans.append(res // x)
            else:
                ans.append(0)
        else:
            if cnt > 1:
                ans.append(0)
            else:
                ans.append(res)

    return ans

if __name__ == '__main__':
    nums = [-1,0,1,2,3]
    print(productExceptSelf(nums))