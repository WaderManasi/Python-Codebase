#Comparison operators or relational operators are used to compare two operands
#and they return a True or False as output.
def print_fun(a,b):
    print(bool(a==b)) ##do a==b
    print(bool(a>b)) ##do a>b
    print(bool(a!=b)) ##do a!=b
    print(bool(a<b)) ##do a<b


def main():
    t=int(input())
    while(t>0):
        x=int(input())
        y=int(input())
        print_fun(x,y)
        t-=1
if  __name__=='main':
    main()