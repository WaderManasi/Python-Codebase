#take input a single line string comprised of string, int, and float. You'll split the string and assign string to s, int to i, and float to f. 
# Print a final string comprised of s and (i+f)

def inPutS():
    a=input()
    ## input in a single line()
    
    s,i,f = a.split(" ")
    ## split the a into three parts: string, integer, and f. 
    int(i)+float(f)
    
    print(s+" "+str(int(i)+float(f))) 
    ##type cast i to int, f to float. Add i with f. Typecast the result to string


def main():
    t=int(input())
    while(t>0):
        inputS()
        t-=1
if  __name__=='main':
    main()