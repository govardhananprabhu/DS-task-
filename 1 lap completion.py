"""
There are some atheletes running in circular ground,you need to find the count of atheletes who completed only 1 lap.You are given with array of integers,which are atheletes,the lap count is equal to count of elements in it.

In des
First line contain integer N,denotes size of array.
Second line contain N space separated integers,denotes athelets.

Ot des
Print the count of atheletes who completed 1 lap.

5
1 2 1 2 3 

1

Exp
From sample
1 and 2 completed 2 laps,3 completed only 1,so count is 1

Hint
Traverse the array and find the count of each element in arr and from that find the count of elements completed 1 lap only. 

H 4
T 2000


"""
N=int(input())
arr = list(map(int,input().split()))
ans=[]
c=0
for i in arr:
    if i not in ans:
        ans.append(i)
        if arr.count(i)==1:
            c+=1
print(c)
