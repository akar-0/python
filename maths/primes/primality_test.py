#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 11:36:26 2020

@author: akar
"""

from primality import primality_test

n= input("Please enter a positive integer:\t")

test = primality_test(int(n))

if test == True:
    print(f"{n} is a prime number!\nIt has no integer factor apart from 1 and "
          "itself")
elif test[1] == None:
    print("0 and 1 are not prime numbers.")
else:
    print(f"{n} is a composite number and its smallest prime factor is {test[1]}")
