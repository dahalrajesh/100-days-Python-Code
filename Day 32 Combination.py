# Write a program to print all the unique combinations of 1,2,3 and 4
import itertools
from itertools import combinations

num=[1,2,3,4]
for i in range(1,len(num)+1):
    comb=itertools.combinations(num,i)
    for combo in comb:
        print(combo)

# print(type(num))
