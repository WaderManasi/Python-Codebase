##date: 7 aug 2020

## Calculate program to find greatest among three numbers

def max_among_three(no1,no2,no3):
    if(no1>no2 and no1>no3):
        print("\nGreatest number is: ",no1)
    else:
        if(no2>no3):
            print("\nGreatest number is: ",no2)
        elif(no3>no2):
            print("\nGreatest number is: ",no3)


############################################################
            
no1=float(input("\nEnter first number: "))
no2=float(input("Enter second number: "))
no3=float(input("Enter third number: "))

max_among_three(no1,no2,no3)
