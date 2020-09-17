
# from math import *
# def fibonaci (n):
#     phi = (1+sqrt(5))/2
#     phi_ = (1-sqrt(5))/2
#     return int((phi**n - phi_**n)/sqrt(5))
def fib(n): 
    F = [[1, 1], 
         [1, 0]] 
    if (n == 0): 
        return 0
    power(F, n - 1) 
      
    return F[0][0] 
  
def multiply(F, M): 
  
    x = (F[0][0] * M[0][0] + 
         F[0][1] * M[1][0]) 
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1]) 
    z = (F[1][0] * M[0][0] + 
         F[1][1] * M[1][0]) 
    w = (F[1][0] * M[0][1] + 
         F[1][1] * M[1][1]) 
      
    F[0][0] = x 
    F[0][1] = y 
    F[1][0] = z 
    F[1][1] = w 
  
def power(F, n): 
  
    M = [[1, 1], 
         [1, 0]] 
  
    # n - 1 times multiply the 
    # matrix to {{1,0},{0,1}} 
    for i in range(2, n + 1): 
        multiply(F, M) 
  
# Driver Code 
# if __name__ == "__main__": 
#     n = 9
#     print(fib(n)) 
  
# # This code is contributed  
# # by ChitraNayal 
# print(fibonaci(int(input)))
x, y = map(int, input().split(' '))

def fibs_seq_holt(n,k):
    return fib(2*k+1)*n % 1000000007

print(fibs_seq_holt(x,y))

# def fibonaci (n):
#     a= []
#     if n==0:
#         a.append(1)
#     if n==1:
#         a.append(1)
#         a.append(1)
#     if (n!=0 and n!=1):
#         a.append(1)
#         a.append(1)
#         for i in range (2, n):
#             a[i] = a[i-1] + a[i-2]
#     return a

# print(fibonaci(10))