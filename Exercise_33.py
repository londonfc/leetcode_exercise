#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 22:37:01 2018

@author: ruicao
"""

class Solution:
    def search(self, nums, target):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not nums or target is None:
            return -1
            
        
        i=0
        j=len(nums)-1
        
        while i<j:
            mid = (j-i)//2+i
            
            if nums[mid]<nums[i] and nums[mid]<nums[j]:
                
                if target>nums[mid]:
                    
                    if target>nums[i]:
                        j=mid-1
                    elif target<nums[i]:
                        i=mid+1
                    else:
                        return i
                
                elif target<nums[mid]:
                    j=mid-1
                    #i=(mid-i)//2+i
                
                else:
                    return mid
            
            elif nums[mid]>=nums[i] and nums[mid]>=nums[j]:
                if target>nums[mid]:
                    i=mid+1
                    #j=(j-mid)//2+mid
                
                elif target<nums[mid]:
                    if target>nums[i]:
                        j=mid-1
                    elif target<nums[i]:
                        i=mid+1
                    else:
                        return i
                
                else:
                    return mid
                
                
            else:
                if target>nums[mid]:
                    i=mid+1
                elif target<nums[mid]:
                    j=mid-1
                else:
                    return mid
        
        if i==j and target == nums[i]:
            return i
            
        return -1


