#In this question we will sum the 
#elements taken as variable arguments and print the result.


def multivar(a, *var): 
    ##*var takes multiple arguments inside it(arr)
    ##print the sum of a+elements of var
    sum=0
    for i in range(0,len(var)):
        sum=sum+var[i]
    print(int(sum)+int(a))

def main():
    t=int(input())
    while(t>0):
        single=int(input())
        multivar(single,4,5,6,7)
        print()
        t-=1

if  __name__=='main':
    main()