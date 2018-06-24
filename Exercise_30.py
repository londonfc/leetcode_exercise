#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 22:37:02 2018

@author: ruicao
"""

class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        
        if words is None or s is None or not words:
            return []
        
        n_words = len(words)
        
        n_word = len(words[0])
        
        if len(s)<(n_words*n_word):
            
            return []
        
        orig = set(words)
        
        bad = set()
        
        word_count = {}
        
        for i in words:
            if i not in word_count.keys():
                word_count[i]=1
            
            else:
                word_count[i]+=1
        
        
        history = word_count.copy()
        
        result = []
        
        
        
        
        for i in range(len(s)-n_words*n_word+1):
            
            if i in bad:
                
                continue
            
            j=i
            
            
            
            while j<=i+(n_words-1)*n_word:
                sub = s[j:j+n_word]
                
                
                if sub not in orig:
                    bad.add(j)  
                
                    break
                    
                
                j+=n_word
                if history[sub]>0:
                    history[sub]-=1
                
                else:
                    break
            
            if sum(history.values())==0:
                result.append(i)
            
            history = word_count.copy()
        
        return result
                    
                    
                    
                    
                    
                    
                
            
    
    
sol=Solution()
s="barfoofoobarthefoobarman"
words = ["bar","foo","the"]
