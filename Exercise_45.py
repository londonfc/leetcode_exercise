#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 22:37:02 2018

@author: ruicao
"""

class Solution:
     def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        
        
       if len(nums)<=1:
            return 0
        
        
        i=0
        count=0
        while i<len(nums):
            maximum = 0
            tmp = 0
            count+=1
            if i+nums[i]>=len(nums)-1:
                break
            
            for j in range(i+1, nums[i]+i+1):
                if maximum< j+nums[j]:
                    maximum = j+nums[j]
                    tmp = j
            i=tmp
                
                    
        return count
                    
                    
                

        
    
sol=Solution()
print(sol.jump([2,3,1,1,4]))
#print(sol.isMatch('mississippi','mis*is*ip*.'))