'''
Problem Statement

Given an array A={a1,a2,…,aN} of N elements, find the maximum possible sum of a

Contiguous subarray
Non-contiguous (not necessarily contiguous) subarray.
Empty subarrays/subsequences should not be considered.

Input Format

First line of the input has an integer T. T cases follow. 
Each test case begins with an integer N. In the next line, N integers follow representing the elements of array A.

Constraints:

1≤T≤10
1≤N≤105
−104≤ai≤104
The subarray and subsequences you consider should have at least one element.

Output Format

Two, space separated, integers denoting the maximum contiguous and non-contiguous subarray. At least one integer should be selected and put into the subarrays (this may be required in cases where all elements are negative).

Sample Input
2 
4 
1 2 3 4
6
2 -1 2 3 4 -5


Sample Output
10 10
10 11
Explanation

In the first case: 
The max sum for both contiguous and non-contiguous elements is the sum of ALL the elements (as they are all positive).

In the second case: 
[2 -1 2 3 4] --> This forms the contiguous sub-array with the maximum sum. 
For the max sum of a not-necessarily-contiguous group of elements, simply add all the positive elements.

'''


def contiguous(x):
    max = 10^-8  
    for i in range( len(nos) ):
        sum = nos[i]
        if sum >max:  # even the last no. can be max, in this case it won't go into the loop so chech here itself
            max = sum
        for j in range( i+1, len(nos) ):
            sum += nos[j]
            if sum > max:
                max = sum            
    return max 
    
def non_contiguous(x):    
    sum = 0
    status =0
    for i in x:
        if i >0:
            sum += i
            status =1            
        else:
            pass
    if status == 0:
        sum = max(nos) #case when all numbers are negative
    return sum
    
        
if __name__ == "__main__":
    n = int( raw_input() ) 
    
    for _ in range(n):  
        
        raw_input()   
        
        nos = map( int, raw_input().split() )
        
        
        if len(nos)==1:
            print nos[0], nos[0]
            
        else:
            print contiguous(nos),
            print non_contiguous(nos)
        