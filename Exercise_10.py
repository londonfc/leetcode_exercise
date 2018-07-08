#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 22:37:02 2018

@author: ruicao
"""

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.myMatch(s, p, 0, 0)
                
    def myMatch(self, s, p, i, j):
        
        if j>len(p)-1:
            
            return i>len(s)-1
        
        if j==len(p)-1:
            
            return i==len(s)-1 and (p[j]=='.' or p[j]==s[i])
        
        if j+1<len(p) and p[j+1]!='*':
            if i>=len(s):
                return False
            
            if p[j]=='.' or p[j]==s[i]:
                return self.myMatch(s,p, i+1, j+1)
            else:
                return False
            
        while i<len(s) and j<len(p) and (p[j]=='.' or p[j]==s[i]):
            if self.myMatch(s, p, i, j+2):
                return True
            i+=1
        
        return self.myMatch(s, p, i, j+2)  
                
                    
                    
                

        
    
sol=Solution()
print(sol.isMatch('ab','.*c'))
#print(sol.isMatch('mississippi','mis*is*ip*.'))