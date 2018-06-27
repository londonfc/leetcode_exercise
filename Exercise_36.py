#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 22:37:02 2018

@author: ruicao
"""

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if not board:
            return False
        
        for i in range(9):
            tmp = set()
            
            for j in range(9):
                if board[i][j] is not '.':
                    if board[i][j] not in tmp:
                        tmp.add(board[i][j])
                    else:
                        return False
                
        for i in range(9):
            tmp =set()
            for j in range(9):
                
                if board[j][i] is not '.':
                    if board[j][i] not in tmp:
                        tmp.add(board[j][i])
                    else:
                        return False
                
        
        for m in range(0,9,3):
            
            for k in range(0, 9, 3):
                tmp=set()
                for i in range(m, m+3, 1):
               
                    for j in range(k, k+3, 1):
                        
                        if board[i][j] is not '.':
                            if board[i][j] not in tmp:
                                tmp.add(board[i][j])
                            else:
                                return False
                    
                
        return True          