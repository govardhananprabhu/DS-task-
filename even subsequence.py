"""
Given an array arr[] consisting of N positive integers, and an integer K, the task is to find the maximum possible even sum of any subsequence of size K. If it is not possible to find any even sum subsequence of size K, then print -1.

H 5 T 1500
tag array

In des
First line contains integer N, size of array.
Second line contains N space separated integers, denotes array elements.
Third line contains integer K,denotes the size of subsequence.

Ot des
Print the value else -1.

5
4 2 6 7 8
3

18

5
5 5 1 1 3
3

-1

5
2 5 1 3 5
3

12

3
2 5 7
1

2

3
3 5 7
-1
Exp
Subsequence having maximum even sum of size K( = 3 ) is {4, 6, 8}.
Therefore, the required output is 4 + 6 + 8 = 18.

Hint
The simplest approach to solve this problem to generate all possible subsequences of size K from the given array and print the value of maximum possible even sum althe possible subsequences of the given array.

"""

#include <bits/stdc++.h> 
using namespace std; 

// Function to find the 
// maximum even sum of any 
// subsequence of length K 
int evenSumK(int arr[], 
			int N, int K) 
{ 

	// If count of elements 
	// is less than K 
	if (K > N) { 
		return -1; 
	} 

	// Stores maximum 
	// even subsequence sum 
	int maxSum = 0; 

	// Stores Even numbers 
	vector<int> Even; 

	// Stores Odd numbers 
	vector<int> Odd; 

	// Traverse the array 
	for (int i = 0; i < N; 
		i++) { 

		// If current element 
		// is an odd number 
		if (arr[i] % 2) { 

			// Insert odd number 
			Odd.push_back(arr[i]); 
		} 
		else { 

			// Insert even numbers 
			Even.push_back(arr[i]); 
		} 
	} 

	// Sort Odd[] array 
	sort(Odd.begin(), Odd.end()); 

	// Sort Even[] array 
	sort(Even.begin(), Even.end()); 

	// Stores current index 
	// Of Even[] array 
	int i = Even.size() - 1; 

	// Stores current index 
	// Of Odd[] array 
	int j = Odd.size() - 1; 

	while (K > 0) { 

		// If K is odd 
		if (K % 2 == 1) { 

			// If count of elements 
			// in Even[] >= 1 
			if (i >= 0) { 

				// Update maxSum 
				maxSum += Even[i]; 

				// Update i 
				i--; 
			} 

			// If count of elements 
			// in Even[] array is 0. 
			else { 
				return -1; 
			} 

			// Update K 
			K--; 
		} 

		// If count of elements 
		// in Even[] and odd[] >= 2 
		else if (i >= 1 && j >= 1) { 

			if (Even[i] + Even[i - 1] 
				<= Odd[j] + Odd[j - 1]) { 

				// Update maxSum 
				maxSum += Odd[j] + Odd[j - 1]; 

				// Update j. 
				j -= 2; 
			} 
			else { 

				// Update maxSum 
				maxSum += Even[i] + Even[i - 1]; 

				// Update i 
				i -= 2; 
			} 

			// Update K 
			K -= 2; 
		} 

		// If count of elements 
		// in Even[] array >= 2. 
		else if (i >= 1) { 

			// Update maxSum 
			maxSum += Even[i] + Even[i - 1]; 

			// Update i. 
			i -= 2; 

			// Update K. 
			K -= 2; 
		} 

		// If count of elements 
		// in Odd[] array >= 2 
		else if (j >= 2) { 

			// Update maxSum 
			maxSum += Odd[j] + Odd[j - 1]; 

			// Update i. 
			j -= 2; 

			// Update K. 
			K -= 2; 
		} 
	} 

	return maxSum; 
} 

// Driver Code 
int main() 
{ 
	int arr[] = { 2, 4, 10, 3, 5 }; 
	int N = sizeof(arr) / sizeof(arr[0]); 
	int K = 3; 
	cout << evenSumK(arr, N, K); 
} 
