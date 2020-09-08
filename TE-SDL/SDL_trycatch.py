try:
    a=int(input("enter 1st no"))
    b=int(input("enter 2nd no"))
    c=a/b
    print("division is: ",c)
except ZeroDivisionError as e:
    print("cannot divide by 0",e)
except ValueError as e:
    print("only inteeger num required",e)
finally:
    print("excecuted succesfully")
