import numpy as np

# Enter your code here. Read input from STDIN. Print output to STDOUT
def array_index(n,n_row,n_col):
    x=np.arange(n).reshape(n_row,n_col)
    print(x[n_row-1])#print elements of last row
    # print(n_col//2)
    print(x[:,n_col//2])#Print elements of middle column
    print(x[:2,-3:])#Print elements overlapping first two rows and last three columns
    
    
    
    
    

if __name__ == '__main__':
    n = int(input())
    n_row = int(input())
    n_col = int(input())
    array_index(n,n_row,n_col)