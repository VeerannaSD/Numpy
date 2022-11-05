import ast
import numpy as np

# Enter your code here. Read input from STDIN. Print output to STDOUT
def array_split(n,n_row,n_col):
    x=np.arange(n)
    z=x.reshape(n_row,n_col)
    res1,res2=np.vsplit(z,2)
    print(res1)
    print(res2)
    

if __name__ == "__main__":
    n = ast.literal_eval(input())
    n_row = ast.literal_eval(input())
    n_col = ast.literal_eval(input())
    array_split(n,n_row,n_col)