#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 22:37:02 2018

@author: ruicao
"""


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
       n = len(nums)-1
        
        if n<1:
            return 
        
        
        while n>0 and nums[n-1]>=nums[n]:
            n-=1
            
            
        if n==0:
            nums = nums.reverse()
            return 
        
        for j in range(len(nums)-1, n-1,-1):
            if nums[j]>nums[n-1]:
                
                nums[n-1], nums[j] = nums[j], nums[n-1]
                break
        
        print(nums)
        nums[n:] = nums[n:][::-1]
        print(nums)
        return
        
    
    
s=Solution()
a=[1,3,2]
s.nextPermutation(a)
print(a)
    

