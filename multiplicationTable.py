#Multiplication table

def multiplicationTable(N):
    ## in is a membership operator that is true if something is a member of sequence
    for i in range(1,11,1): 
        ## i in range(x,y,z) means i goes from x to y-1 and increments z steps in each iteration
        print(i*N, end=" ") 
        ## Separating by spaces using end =" "

def main():
    t=int(input())
    while(t>0):
        n=int(input())
        multiplicationTable(n)
        print()
        t-=1
if  __name__=='main':
    main()