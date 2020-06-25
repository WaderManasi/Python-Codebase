#take input of 3 strings. The strings are in separate lines. 
# You need to take the inputs and print the outputs.

def inPutCat():
    a=str(input());
    b=str(input());
    c=str(input());
    print(a,b,c) 
    ## comma is used as it automatically separates the variables by a space. 
    ## + can also be used to concatenate but it would require manual spaces to print the words with spaces between them.


def main():
    t=int(input());
    while(t>0):
        inPutCat();
        t-=1;
if  __name__=='main':
    main();