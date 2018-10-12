#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s1 = set([1, 1, 2, 2, 3, 3])
print(s1) # {1, 2, 3}
s2 = set([2, 3, 4])
print(s1 & s2) # {2, 3}
print(s1 | s2) # {1, 2, 3, 4}
