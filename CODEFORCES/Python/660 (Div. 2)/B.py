from __future__ import division, print_function
# import threading
# threading.stack_size(2**27)
# import sys
# sys.setrecursionlimit(10**7)
# sys.stdin = open('inpy.txt', 'r')
# sys.stdout = open('outpy.txt', 'w')
from sys import stdin, stdout
import bisect            #c++ upperbound
import math
import heapq
i_m=9223372036854775807
def inin():
    return int(input())
def stin():
    return input()
def spin():
    return map(int,stin().split())
def lin():                           #takes array as input
    return list(map(int,stin().split()))
def matrix(n):
    #matrix input
    return [list(map(int,input().split()))for i in range(n)]

################################################
def count2Dmatrix(i,list):
    return sum(c.count(i) for c in list)

def modinv(n,p):
    return pow(n,p-2,p)

def GCD(x, y): 
    x=abs(x)
    y=abs(y)
    if(min(x,y)==0):
        return max(x,y)
    while(y): 
        x, y = y, x % y 
    return x
def Divisors(n) : 
    l = []  
    for i in range(1, int(math.sqrt(n) + 1)) :
        if (n % i == 0) : 
            if (n // i == i) : 
                l.append(i) 
            else : 
                l.append(i)
                l.append(n//i)
    return l
prime=[]
def SieveOfEratosthenes(n): 
    global prime
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    f=[]
    for p in range(2, n): 
        if prime[p]: 
            f.append(p)
    return f
q=[]       
def dfs(n,d,v,c):
    global q
    v[n]=1
    x=d[n]
    q.append(n)
    j=c
    for i in x:
        if i not in v:
            f=dfs(i,d,v,c+1)
            j=max(j,f)
            # print(f)
    return j
# d = {}
 
"""*******************************************************"""
for _ in range(inin()):
    n = inin()
    
    l = []
    x = (n+3)//4
    for i in range(n-x):
        l.append('9')
    for i in range(x):
        l.append('8')
    print("".join(l))

    # temp= 0

    # if n%2==0:
    #     if n%4==0:
    #         temp = n - n//4
    #         l = ['9']*temp
    #         l += ['0']*(n//4)
    #     else:
    #         temp = (n - 2)//4
    #         l = ['9']*(n - temp - 1)
    #         l.append('8')
    #         l += ['0'] * temp
    #     # print("".join(l))

    # else:
    #     if n%4==1:
    #         temp = (n - 1)//4
    #         l = ['9'] * (n - temp -1)
    #         l += ['8']
    #         l += ['0']*temp
    #     else:
    #         temp = (n - 3)//4
    #         l = ['9'] * (n - temp -1)
    #         l += ['8']
    #         l += ['0']*temp
    # print("".join(l))
