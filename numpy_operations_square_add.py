import numpy as np

# Enter your code here. Read input from STDIN. Print output to STDOUT
def array_oper(num1,num2):
    y=np.arange(num1,num2+1).reshape(2,3)
    ysquare=y**2
    ysquare_plus_5=ysquare+5
    print(ysquare_plus_5)
    # print(y)
    
    
    
    
    

if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    array_oper(num1,num2)