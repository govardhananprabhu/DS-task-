"""
There is an atheletics competetion in your school,you need to figure out who got first,second and third.
you are given with array of integers,which are atheletes,the element that occurs twice first considered as
first,second and so on.If no one completed first lap print -1,if first place founded but 2nd 3rd can't then print it as -1.see explanation for better example.

In des
First line contain integer N,denotes size of array.
Second line contain N space separated integers,denotes athelets.

Ot des
Print the space separated fist,second and third atheletes

5
1 2 1 2 3 

1 2 -1

5
1 2 1 4 3

1 -1 -1
Exp
From sample
1 is repeated twice first and then 2,3.

Hint
Traverse the array and find the first 3 element repeated twice.

H 4
T 2000


"""
N=int(input())
arr = list(map(int,input().split()))
ans=[]
for i in arr:
    if i not in ans:
        if(arr.count(i)>1):
            ans.append(i)
for i in arr:
    if arr.count(i)==1:
        ans.append('-1')
if(ans[0]==-1):
    print('-1')
else:
    print(*ans[:3])
