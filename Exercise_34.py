#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 22:37:02 2018

@author: ruicao
"""

class Solution:
    def searchRange(self, nums, target):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not nums or target is None:
            return [-1, -1]
        
        i=0
        j=len(nums)-1
        first_found=0
        
        while i<j:
            mid = (j-i)//2+i
            
            if nums[mid]>target:
                j=mid-1
            elif nums[mid]<target:
                i=mid+1
            else:
                first_found=mid
                break
          
        if i>=j: 
            
            if nums[i]==target:
                return [i, i]
            else:
                return [-1, -1]
        
        result=[]
        i=0
        j=first_found
        while nums[i]!=target and i<j:
            mid = (j-i)//2+i
            if nums[mid]==target:
                j=mid
            else:
                i=mid+1
        
        result.append(i)
        
        i=first_found
        j=len(nums)-1
        while nums[j]!=target and i<j:
            mid=(j-i)//2+i+1
            if nums[mid]==target:
                i=mid
            else:
                j=mid-1
        result.append(j)
        
        return result

sol = Solution()
nums=[2,2]
target =4
print(sol.searchRange(nums, 1))