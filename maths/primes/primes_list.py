#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 23:42:01 2020

@author: akar
"""

def primes_list(rank):
    """
    Parameters
    ----------
    rank : positive integer strictly superior to 2

    Returns
    -------
    A list retrieving:
        pin: (integer) amount of prime numbers inferior or equal to rank
        target: (integers ordered list) prime numbers inferior or equal to rank

    """
    from math import sqrt
    prime = 3
    target = {n for n in range(3, (rank + 1), 2)}
    while prime <= sqrt(rank):
        prime_multis = {n for n in\
                        range((2 * prime), (max(target) + 1), prime)}
        target = target.difference(prime_multis)
        target = sorted(list(target))
        for x in target:
            if x > prime:
                prime = x
                target = set(target)
                break
    target.add(2)
    target = sorted(list(target))
    pin = len(target)
    return [pin, target]
