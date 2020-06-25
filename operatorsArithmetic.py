#Arithmetic Operations:
#a. Add ("+"): Adding X and Y.
#b. Subtract ("-"): Subtracting X and Y.
#c. Multiply ("*"): Multiply X and Y.
#d. Divide ("/"): Divide X by Y.
#e. Multiplying X, Y times ("**"): X raised to power Y.
#f. Divide and floor the result ("//"): Divide and result is in integer form.

def print_fun(x,y):
    print(str(int(x)+int(y)))
    print(str(int(x)-int(y)))
    print(str(int(x)*int(y)))
    print(str(int(x)/int(y)))
    print(x**y)
    print(x//y)


def main():
    t=int(input());
    while(t>0):
        x=int(input());
        y=int(input());
        print_fun(x,y);
        t-=1;
if  __name__=='main':
    main();