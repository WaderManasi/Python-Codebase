#'is' and 'is not' operators are coding equivalents of '==' and '!='  respectively.
#  However, there are some minor differences that will be covered in the second module.

# 'in' operator is used to check if something is in some other thing, like 5 in range(2,6). 
# It's useful in loops.

def number_present(arr,n):
    for i in range(len(arr)):
        if (arr[i]==n):
            return "True"
    return "False"
    


def main():
    t=int(input());
    while(t>0):
        arr=input()
        arr=arr.split(" ")
        for i in range(len(arr)):       #initial array
            arr[i]=int(arr[i])

        brr=input()
        brr=brr.split(" ")
        for in range(len(brr)):
            brr[i]=int(brr[i])          #numbers to check whether prsent or not
        
        for i in range(len(brr)):
            if number_present(arr,brr[i]):
                print("True")
            else:
                print("False")
        t-=1;
if  __name__=='main':
    main();