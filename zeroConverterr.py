# You are given a number n. 
# The number n can be negative or positive. 
# If n is negative, print numbers from n to 0 by adding 1 to n. 
# If positive, print numbers from n-1 to 0 by subtracting 1 from n.

def pos(n):
    while(n-1>=0):
        print(n-1,end=" ")
        n-=1
        
    
def neg(n):
    while(n<=0):
        print(n,end=" ")
        n+=1

def main():
    t=int(input())
    while(t>0):
        n=int(input())
        if(n>0):
            pos(n)
        elif(n<0):
            neg(n)
        else:
            print("already Zero",end=" ")
        print()
        t-=1

if  __name__=='main':
    main()