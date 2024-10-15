"""
Write a program to print the given list in reverse order.
Sample Input:
10 20 30 40 50
Sample Output:
50 40 30 20 10 

"""
elements = input().split()  
reversed_elements = elements[::-1]
print(" ".join(reversed_elements))
