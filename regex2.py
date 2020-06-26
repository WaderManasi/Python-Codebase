#The validation rules are as follows:
#The string is valid only if it starts with lowercase characters, followed by special characters !@#$% followed by numbers.
#In any other case the string is not valid

import re

def patMatcher(str):
    pat=('[a-z]+[!@#$%]+[0-9]')
    match=re.search(pat,str)
    if(match):
        print("True")
    else:
        print("False")

def main():
    t=int(input())
    while(t>0):
        s=input()
        patMatcher(s)
        t-=1
if  __name__=='main':
    main()