#Python functions allows us to create anonymous functions using the lambda keyword. 
#These functions are small one line functions that don't use the def keyword.
#In this question we will create an anonymous function to print a to power b.


power=lambda a,b :a**b

def main():
    t=int(input())
    while(t>0):
        base=int(input())
        exp=int(input())
        print(power(base,exp))
        t-=1
if  __name__=='main':
    main()