"""
Power Set Power set P(S) of a set S is the set of all subsets of S. For example S = {a, b, c} then P(s) = {{}, {a}, {b}, {c}, {a,b}, {a, c}, {b, c}, {a, b, c}}.

If S has n elements in it then P(s) will have 2^n elements
EXP
Set  = [a,b,c]
power_set_size = pow(2, 3) = 8
Run for binary counter = 000 to 111

Value of Counter            Subset
    000                    -> Empty set
    001                    -> a
    010                    -> b
    011                    -> ab
    100                    -> c
    101                    -> ac
    110                    -> bc
    111                    -> abc

Hin
We can iterate a loop over 0 to the length of the set to obtain and generate all possible combinations of that string with the iterable length. The program below will give the implementation of the above idea.
"""
from itertools import combinations 
def print_powerset(string): 
    for i in range(0,len(string)+1): 
        for element in combinations(string,i): 
            print(''.join(element)) 
N=int(input())
string=input().split()
print_powerset(string)
