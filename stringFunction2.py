# s.lower(), s.upper(): returns the lowercase or uppercase version of the string.
# s.startswith('string2'), s.endswith('string2'): tests if string starts or ends with the given string2.

def print_input(a):
    b = a.lower()
    if(b.startswith("one")):  # use b.startswith() and b.endswith()
        print ("Yes")
    else:
        print ("No")

def main():
    t=int(input())
    while(t>0):
        str=input()
        print_input(str)

        t-=1
if  __name__=='main':
    main()