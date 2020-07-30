"""
Question
Assume you are the anivirus specialist,you need to found the virus in the given range.
Given a number N, virus is all numbers in range from 1 to N having exactly 3 divisors.

Input description
First line has integer denoting the range
Output description
print the virus till the range

Explanation
Input : N = 16
Output : 4 9
4 and 9 have exactly three divisors.
Divisor

Input
16
Output
4 9

Input
3
Output
-1

Input
99
Output
4 9 25 49

Input
10
Output
4 9

Input
1
Output
-1

HINT
We can generate all primes within a set using any sieve method efficiently and then we should all primes i, suct that i*i <=N.
Solution:"""
def numbersWith3Divisors(n):  
   
    prime=[True]*(n+1);  
    prime[0] = prime[1] = False; 
    p=2; 
    while (p*p<=n):
        if (prime[p] == True): 
            for i in range(p*2,n+1,p): 
                prime[i] = False;  
        p+=1;   
    i=0; 
    while (i*i <= n):  
        if (prime[i]): 
            ans.append(i*i); 
        i+=1; 
  
n = int(input())
ans=[]
numbersWith3Divisors(n);
if(len(ans)==0):
    print(-1)
else:
    print(*ans)
