"""
Question
There is a placement drive in your college,you need to select on who performed well,
there is a array of integers and k,find which element present k times first is got
selected.

Input description
First line has list of integers
Second line has integer k

Output description
print the selected element if not print -1

Explanation
Input: {1, 7, 4, 3, 4, 8, 7},
k = 2
Output: 7
Both 7 and 4 occur 2 times.
But 7 is the first that occurs 2 times

Input
1 1 1 1 1 1
1
Output
-1

Input
1 2 3 4 5 4 3 2 1
2
Output
1

Input
1 2 3 3 2 1 1 2 3
3
Output
1

Input
3 2 45 5 44 2 2 2 1 1
4
Output
2

Input
1
2
Output
-1
Hint
By using two loops, count the number of times a number appears in the array.
Solution:"""
def firstElement(arr, n, k): 

    count_map = {}; 
    for i in range(0, n): 
        if(arr[i] in count_map.keys()): 
            count_map[arr[i]] += 1
        else: 
            count_map[arr[i]] = 1
        i += 1
      
    for i in range(0, n):  
  
        if (count_map[arr[i]] == k): 
            return arr[i] 
        i += 1

    return -1

if __name__=="__main__": 
  
    arr = list(map(int,input().split())) 
    n = len(arr) 
    k = int(input())
    print(firstElement(arr, n, k)) 
