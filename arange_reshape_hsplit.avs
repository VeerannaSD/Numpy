import numpy as np

# Enter your code here. Read input from STDIN. Print output to STDOUT
def array_split(i,r,c):
    #Write your code below
    x=np.arange(i)
    y=x.reshape(r,c)
    a,b=np.hsplit(y,2)
    print(a,b)
    

if __name__=="__main__":
    i=int(input())
    r,c = list(map(int,input().split()))
    array_split(i,r,c)