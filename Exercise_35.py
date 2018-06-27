#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 22:37:03 2018

@author: ruicao
"""

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or target is None:
            return 0
        
        i=0
        j=len(nums)-1
        
        while i<j:
            mid = (j-i)//2+i
            
            if nums[mid]>target:
                j=mid
            elif nums[mid]<target:
                i=mid+1
        
            else:
                return mid
            
        if i>=j:
            if nums[i]<target:
                return i+1
            return i
