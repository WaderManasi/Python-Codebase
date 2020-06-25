#You are given a string str, 
# you need to print its characters at even indices(index starts at 0).

def stringJumper(N):
    for i in range(0,len(str),2):
    ## from 0 to length of str and skip 2
        print(str[i], end=" ")
        ##printing character and separating characters by nothing


def main():
    t=int(input())
    while(t>0):
        string=input()
        stringJumper(string)
        print()     #separating testcases by newline
        t-=1
if  __name__=='main':
    main()