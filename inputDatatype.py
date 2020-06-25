
def inPut():
    #Take input and assign the input to a,b,c,d. 
    # Typecast as type() will produce wrong answer without it
    a=int(input()); #a is integer type
    b=str(input()); #b is string type
    c=float(input()); #c is float type
    d=bool(input());  #d is boolean type
    
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))
    print(d, type(d))


def main():
    t=int(input())
    while(t>0):
        inPut()
        t-=1
if  __name__=='main':
    main()