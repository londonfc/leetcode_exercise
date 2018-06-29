#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 22:37:02 2018

@author: ruicao
"""

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates or target is None:
            return [[]]
        
        
        self.sort(candidates, 0, len(candidates)-1)
        result = []
        self.combination(candidates, 0, target, [], result)
        return result
        
    def combination(self, nums, start, target, values, result):
        
        
        if target==0:
            result.append(values)
            return
        
        for i in range(start, len(nums)):
            if nums[i]>target:
                return
            
            self.combination(nums, i, target-nums[i], values+[nums[i]], result)
    
    def solvable(self, nums, target, i):
        if not nums or target is None:
            return False
        
        if target<nums[0]:
            return False
        
        
        if target%i == 0 or (target-i) in nums or (target%i) in nums:
            return True
        
        return self.solvable(nums, target-i, i)
    
    def sort(self, a, lo, hi):
        if lo>=hi:
            return
        k=self.partition(a, lo, hi)
        self.sort(a, lo, k-1)
        self.sort(a, k+1, hi)
        
        
    def partition(self, a, lo, hi):
        if lo>=hi:
            return a
        
        i=lo
        j=hi
        while True:
            while a[i]<a[hi]:
                i+=1
            while a[j]>=a[hi]:
                j-=1
            if i>=j:
                break
            a[i],a[j] = a[j], a[i]
            
        a[hi], a[j] =  a[j], a[hi]
        
        return j
    
sol=Solution()
print(sol.combinationSum([2,3,6,7],7))