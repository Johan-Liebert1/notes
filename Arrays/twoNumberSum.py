'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]'''

def twoSum(self, nums, target):
    
    table1 = {}
    ret = []

    for index, element in enumerate(nums):
        table1[target - element] = index


    for i,e in enumerate(nums):
        
        if e in table1 and (i != table1[e]):
            ret.append(i)
            ret.append(table1[e])
            

            return ret

    
    
