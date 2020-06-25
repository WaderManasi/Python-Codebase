#Input Format:
#First line of input contains number of testcases T. For each testcase, there will be a single containing value of j_angry and s_angry.
#Output Format:
#For each testcase, in a new line, print True or False, depending on input.

def friends_in_trouble(a_angry, b_angry):
    if(a_angry == b_angry):
        print("True")
    else:
        print("False")

def main():
    t=int(input())
    while(t>0):
        string=input()
        one=string[0]
        two=string[1]
        if(one=='True'):
            one=True
        else:
            one=False
        
        if(two=='True'):
            two=True
        else:
            two=False

        friends_in_trouble(one,two)
        t-=1
if  __name__=='main':
    main()