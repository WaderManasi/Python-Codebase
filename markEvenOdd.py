#Given a positive integer x. 
# The task is to check if it is even or odd (Any number that gives zero as remainder when divided by 2 is an even number)

def checkOddEven(x):
    if(x % 2 is 0):
      return True
    else:
        return False

def main():
    t=int(input())
    while(t>0):
        x=input()

        if(checkOddEven(x)):
            print("Even")
        else:
            print("Odd")
        t-=1
if  __name__=='main':
    main(); 