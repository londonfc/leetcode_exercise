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
            return nums
        
        memo = {}
        result = []
        
        for i in range(0, 10):
            memo[i]=0
            
        
        
        memo[nums[n]]+=1
        while n>0 and nums[n-1]>=nums[n]:
            n-=1
            memo[nums[n-1]]+=1
            
        if n==0:
            return self.dict_to_list(memo)
        
        for j in range(nums[n-1]+1, 10):
            if memo[j]!=0:
                memo[nums[n-1]]+=1
                memo[j]-=1
                nums[n-1] = j
                break
        
        return nums[0:n]+self.dict_to_list(memo)
        
    
    def dict_to_list(self, dict):
        a=[]
        for i in dict.keys():
            a=a+[i]*dict[i]
            
        return a
    
s=Solution()
a=[16,27,25,23,25,16,12,9,1,2,7,20,19,23,16,0,6,22,16,11,8,27,9,2,20,2,13,7,25,29,12,12,18,29,27,13,16,1,22,9,3,21,29,14,7,8,14,5,0,23,16,1,20]
print(s.nextPermutation(a))