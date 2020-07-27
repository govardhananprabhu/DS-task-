"""
Question
Given an input string and a list of words, find out if the input string can be
segmented into a space-separated sequence of dictionary words. See following examples
for more details.

Input description
First line has string
Second line has list of string

Output description
Print yes or no


Input
i l u
ilu
Output
yes

Input
a e i o u
aeiou
Output
yes

Input
a e i o u s t r
www
Output
no

Input
water milk grape fruits
milkwater
Output
yes


Solution:"""
class Solution(object):
   def wordBreak(self, s, wordDict):
      dp = [[False for i in range(len(s))] for x in range(len(s))]
      for i in range(1,len(s)+1):
         for j in range(len(s)-i+1):
            if s[j:j+i] in wordDict:
               dp[j][j+i-1] = True
            else:
               for k in range(j+1,j+i):
                  if dp[j][k-1] and dp[k][j+i-1]:
                     dp[j][j+i-1]= True
      return dp[0][len(s) - 1]
ob1 = Solution()
l=input().split()
s=input()
if(ob1.wordBreak(s,l)):
    print('yes')
else:
    print('no')
