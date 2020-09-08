##date: 7 aug 2020

## Calculator program

def add(no1,no2):
    return no1+no2

def sub(no1,no2):
    return no1-no2

def mul(no1,no2):
    return no1*no2;

def div(no1,no2):
    if no2==0.0:
        print("\nIllegal operation :divide by zero")
    else:
        return no1/no2

no1=float(input("\nEnter first number: "))
no2=float(input("\nEnter second number: "))

print("\n1] Addition\n2] Subtraction\n3] Multiplication\n4] Division")
choice=int(input("Select operation to be performed [1,2,3,4 ?]: "))

while True:
    if(choice==1):
        print("\nAddition is: ",add(no1,no2))
        break
    elif(choice==2):
        print("\nSubtraction is: ",sub(no1,no2))
        break
    elif(choice==3):
        print("\nMultiplication is: ",mul(no1,no2))
        break
    elif(choice==4):
        print("\nDivision is: ",div(no1,no2))
        break
