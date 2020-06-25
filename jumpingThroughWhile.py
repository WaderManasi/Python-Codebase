#Given a positive integer x, the task is to print the numbers 
#from 1 to x in the order as 12, 22, 32, 42, 52, ... (in increasing order).

def printIncreasingPower(x):
    # Loop to jump in powers of 2
    i=1
    while(i*i<=x):
        print (i*i, end = " ")
        i+=1
        
def main():
    t=int(input())
    while(t>0):
        n=int(input())
        printIncreasingPower(n)
        print()
        t-=1

if  __name__=='main':
    main()

