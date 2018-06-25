#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 22:37:02 2018

@author: ruicao
"""

class Solution:
    def findSubstring(self, s):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        
        if s is None:
            return 0
        
        result = 0
        record = []
        record.append(-1)
        
        for i in range(len(s)):
            
            if s[i] is '(':
                record.append(i)
                
            else:
                record.pop()
                
                if len(record)>0:
                    result = max(result, i-record[len(record)-1])
                    
                
                else:
                    record.append(i)
                    
                    
        return result

sol = Solution()
print(sol.findSubstring('(()'))