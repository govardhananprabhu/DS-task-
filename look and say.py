"""
Find the n’th term in Look-and-say (Or Count and Say) Sequence. The look-and-say sequence is the sequence of below integers:
1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, …

In des
First line contain integer N,denotes the range

Ot des
Print the nth term

3
21

5
111221

4
1211


10
13211311123113112211


1
1

Exp
The first term is "1"

Second term is "11", generated by reading first term as "One 1" 
(There is one 1 in previous term)

Third term is "21", generated by reading second term as "Two 1"

Fourth term is "1211", generated by reading third term as "One 2 One 1" 

and so on

Hint
The idea is simple, we generate all terms from 1 to n. First two terms are initialized as “1” and “11”, and all other terms are generated using previous terms. To generate a term using previous term, we scan the previous term. While scanning a term, we simply keep track of count of all consecutive characters. For sequence of same characters, we append the count followed by character to generate the next term.

H-7
T-2500

"""
def countnndSay(n): 
      
    # Base cases 
    if (n == 1): 
        return "1"
    if (n == 2): 
        return "11"
    s = "11" 
    for i in range(3, n + 1): 

        s += '$'
        l = len(s) 
  
        cnt = 1 
        tmp = ""  
 
        for j in range(1 , l): 

            if (s[j] != s[j - 1]):  
                tmp += str(cnt + 0) 
                tmp += s[j - 1] 
                cnt = 1
            else: 
                cnt += 1
        s = tmp 
    return s
N = int(input())
print(countnndSay(N)) 
