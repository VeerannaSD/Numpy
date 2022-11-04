import numpy as np

# Enter your code here. Read input from STDIN. Print output to STDOUTd

def array_attributes(l):
    #write your code here
    y=np.array(l)
    print(type(y))
    print(y.ndim)
    print(y.shape)
    print(y.size)
    print(y.dtype)
    print(y.itemsize)
    
    
    

if __name__=="__main__":
    r=int(input())
    l=[]
    for i in range(r):
        n = list(map(int,input().split()))
        l.append(n)
    array_attributes(l)