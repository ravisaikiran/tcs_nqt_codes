m=int(input("Enter the no. of elements for the list: "))
l=[]
out=0
for i in range(m):
    l.append(int(input()))
for i in range(m):
    arr=l[i+1:]
    s=0
    for j in range(len(arr)):
        s+=arr[j]
        if s==0:
            out=1 
            break
print(out)
"""Example-1:
Input:
4
{6,-2,3,-1)

Output:
1
Example-2:
Input:
5
(5,1,2,3,-4)
Output:
0
Explanation:

In example-1, the number list is 6,-2,3,-1.here (-2) + 3

+(-1) =0. So we can get consecutive numbers in Arr[] and its sum is 0. Hence the output is 1. In example-2, the number list is 5, 1, 2, 3,-4. Any consecutive numbers cannot give 0 sum. Hence the output is 0.
""""
