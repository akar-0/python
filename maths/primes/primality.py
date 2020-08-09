#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 10:30:20 2020

@author: akar
"""

def primality_test(number):
    """
    A primality test algorithm.
    
    Parameters
    ----------
    number : integer
             positive integer

    Returns
    -------
    -If number is a prime number, returns True.
    -If number is not a prime number, returns a tuple of two elements:
        - False
        - If number is a composite number, the second element of the tuple is
        its smallest prime factor; if number is 0 or 1, the second element of
        the tuple is False.
   
    """
    
#This code could be much shorter and readable if it started right first with
#The second while loop; the first conditions are only useful to simplify
#basic calculations, that in all cases don't require much resources
#A test to check if the input is actually an integer should be run first

    from math import sqrt
    nbr = int(number)
    nbr_str = str(nbr)
    if (nbr == 1 or nbr == 0):
        return (False, None)
    elif nbr in [2, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
        return True
    elif (int(nbr_str[-1:]) in {0, 2, 4, 6, 8}):
        return(False, 2)
    elif (nbr_str[-1:] == '5'):
        return(False, 5)
    elif (nbr == 9):
        return(False, 3)
    else:
        list_chars = []
        for char in nbr_str:
            list_chars.append(char)
        while len(list_chars) > 1:
            list_figs = []
            for char in list_chars:
                list_figs.append(int(char))
            sum_figs = sum(list_figs)
            strg_sum = str(sum_figs)
            list_chars = []
            for char in strg_sum:
                list_chars.append(char)
        if sum_figs in {3, 6, 9}:
            return (False, 3)
        else:
            sqrt_n = int(sqrt(nbr))
            if sqrt(nbr) == sqrt_n :
                return (False, sqrt_n)
            
            else:
                target = {n for n in range(7, (sqrt_n), 2)}
                three_multiples = {n for n in range(3, sqrt_n, 3)}
                five_multiples = {n for n in range(5, sqrt_n, 5)}
                target = target - three_multiples - five_multiples
                p = 7
                sqr_target = int(sqrt(max(target)))
                while p <= sqr_target:
                    target = set(target)
                    p_multis = {n for n in range((2 * p), (max(target) + 1), p)}
                    target = target.difference(p_multis)
                    target = sorted(list(target)) 
                    for x in target:
                        if x > p:
                            p = x
                            break
                target = sorted(list(target)) #is it necessary in any case?? seems that, casually, not... 
                for n in target:
                    if nbr % n == 0:
                        return (False, n)
                        break #required in order to give up the if loop?
                    else:
                        return True
