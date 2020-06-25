#Logical operators are and, or, not. They are used in condition checking.
#Example: a and b checks if both a and b are True. First a is checked then b.
#a or b checks if either of a or b is True. If one is True; it doesn't check for other.
#not a complements the boolean value of a

def print_fun(a,b):
    print(a and b) ## do a and b
    print(a or b) ## do a or b
    print(not a) ## do not a


def main():
    t=int(input())
    while(t>0):
        x=int(input())
        y=int(input())
        print_fun(x,y)
        t-=1
if  __name__=='main':
    main()