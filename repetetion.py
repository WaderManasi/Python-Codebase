#To print string n number of types without using Loops

def print_fun(string,x):
    print(string*x);


def main():
    t=int(input());
    while(t>0):
        string=input();
        x=int(input());
        print_fun(string,x);
        t-=1;
if  __name__=='main':
    main();