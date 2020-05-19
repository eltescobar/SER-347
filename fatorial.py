# -*- coding: utf-8 -*-
"""
Created on Tue May 19 12:47:40 2020

@author: eltes
"""

def Fatorial(num):
    produto = 1

    while(num > 0):
        produto = produto * num

        num = num - 1

    return produto