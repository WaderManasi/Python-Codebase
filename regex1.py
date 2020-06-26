#Provided a string str in which you
#have to find all the numbers and print them.

import re

def numberMatcher(str):
    pat=re.compile('[0-9]+')
    match=re.findall(pat,str) 
    ##find all finds all the matched texts and returns a list
    if(match): 
        for i in match:
            print(i, end=" ")
    else:
        print(-1,end="")

def main():
    t=int(input())
    while(t>0):
        s=input()
        numberMatcher(s)
        t-=1
if  __name__=='main':
    main()