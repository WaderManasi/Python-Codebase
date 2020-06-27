# Modules refer to files containing already compiled Python statements
#and definitions. This allow us to break down large number of code lines into 
#group of manageable files.
#You are required to print values of pi constant and e constant in math library.


import math

def math_func():
    print("pi = ",math.pi, "\ne = ",math.e)

def main():
    t=int(input())
    while(t>0):
        math_func()
        t-=1

if __name__=='main':
    main()