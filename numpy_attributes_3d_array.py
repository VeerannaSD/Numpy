import numpy as np

# Enter your code here. Read input from STDIN. Print output to STDOUT
def array_3d(n, x, y, z):
    #Write your code below
    np.random.seed(100)
    x1=np.random.normal(loc=5,scale=2.5,size=n)
    x2=np.random.rand(x,y,z)
    A=(x1.size)*(x1.itemsize)
    print(A)
    print(x2)
    

if __name__ == "__main__":
    n=int(input())
    x, y, z=list(map(int,input().split()))
    array_3d(n, x, y, z)