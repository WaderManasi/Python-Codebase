#Given two integer variables a and b, and a flag which is boolean. 
# The task is to check the status and return accordingly.
#Return "True" if either a or b (one of them) is positive. 
# Except if the flag is True, then return True only if both of the variables a and b are negative.

def check_status(a, b, status):
    if ((a<0) and (b<0 ))and (status==True):
        return(True)
    elif (a<0 and b>0) and (status==False):
        return(True)
    elif(a>0 and b<0)and (status==False):
        return(True)
    else:
        return(False)

def main():
    t=int(input())
    while(t>0):
        a=int(input())
        b=int(input())
        flag=input()

        if(flag=="True"):
            flag=True
        else:
            flag=False

        if(check_status(a,b,flag)):
            print("True")
        else:
            print("False")  
        t-=1
if  __name__=='main':
    main()