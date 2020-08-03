"""
Mohan and thouheed playind finding max digit,the rule is simple one should hide the
max digit in string which has both digits and characters,the other should find the
max digit,thouheed hides the digit help mohan to find it.

Input description
First line has integer denoting size of string
Second line has string
Output description
print the max digit

Explanation
Input : 100klh564abc365bg
Output : 564
Maximum numeric value among 100, 564 
and 365 is 564.

Input
17
100klh564abc365bg
Output
564

Input
7
str9rts
Output
9

Input
2
34
Output
34

Input
5
12345
Output
12345

Input
11
abchsd0sdhs
Output
0

"""
def extractMaximum(ss):
    num, res = 0, 0
    for i in range(len(ss)):
        if ss[i] >= "0" and ss[i] <= "9":
            num = num * 10 + int(int(ss[i]) - 0)
        else:
            print(res,num)
            res = max(res, num)
            num = 0
    return max(res, num) 

N=int(input()) 
ss = input()
print(extractMaximum(ss)) 

