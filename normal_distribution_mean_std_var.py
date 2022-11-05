import ast
import numpy as np

# Enter your code here. Read input from STDIN. Print output to STDOUT
def array_oper(n,m,sd):
    np.random.seed(100)
    x=np.random.normal(loc=m,scale=sd,size=n)
    # print(x.mean())
    print(np.mean(x))
    # print(x.std())
    print(np.std(x))
    # print(x.var())
    print(np.var(x))
    
    
    
    

if __name__ == '__main__':
    num = ast.literal_eval(input())
    mean = ast.literal_eval(input())
    sd = ast.literal_eval(input())
    array_oper(num,mean,sd)