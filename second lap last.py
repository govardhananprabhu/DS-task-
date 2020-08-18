"""
There are some Atheletes running in a ground,Given an array of integers which denotes atheletes, find the last athelete who started runing second lap in it.The last athelete is the element that occurs more than once and whose index of last occurrence.If no one started print -1.

In des
First line contain N integer,denotes size of array.
Second line contain N space separated integers,denotes atheletes.

Ot des
Print the athelete who started second lap last.

7
10 5 3 4 3 5 6

5


9
6 10 5 4 9 120 4 6 10

4



Exp
From sample
3 is the last element that repeats.

Hint
Traverse the array, once we find an element that repeats last, print the element.

H 5
T 2000

"""
N=int(input())
arr = list(map(int,input().split()))
ans=[]
for i in arr:
    if i not in ans:
        if(arr.count(i)>1):
            ans.append(i)
if(len(ans)==0):
    print('-1')
else:
    print(ans[-1])

