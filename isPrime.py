#Check wheather number is prime or not

def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return False
    return True

def main():
    t=int(input())
    while(t>0):
        x=int(input())
        isPrime(x)
        t-=1
        
if  __name__=='main':
    main()