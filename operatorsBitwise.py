#Bitwise operators are useful when we want to work with bits


def print_fun(a,b,c):
    print(a^a)
    print(c^b)
    print(a&b)
    print(c|(a^a))
    print(~(c^b))


def main():
    t=int(input())
    while(t>0):
        x=int(input())
        y=int(input())
        z=int(input())
        print_fun(x,y,z)
        t-=1
if  __name__=='main':
    main()