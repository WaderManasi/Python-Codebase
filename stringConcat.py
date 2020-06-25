#Concatenating two string inputs

def print_fun(string1, string2):
    print (string1 + string2)

def main():
    t=int(input());
    while(t>0):
        string1=input()
        string2=input()
        print_fun(string1,string2)
        t-=1
    
if __name__=='main':
    main();