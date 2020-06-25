#While loop in Python is same as like in CPP and Java,
#  but, here you have to use ':' to end 
# while statement (used to end any statement). 
# While loop is used to iterate same as for loop, except that in while loop you can customize jump of steps in coupling with variable used to loop, after every iteration, unlike in for loop (you cannot customize jump according to the variable you are using to loop through).

def printInDecreasing(x):
    
    while(x >= 0):
        print(x,end=" ")
        x -= 1

def main():
    t=int(input())
    while(t>0):
        n=int(input())
        printInDecreasing(n)
        print()
        t-=1

if  __name__=='main':
    main()