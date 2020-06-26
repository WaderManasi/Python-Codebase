
def trim(str):
    ans=str.strip()
    return ans     # use str.strip() here to truncate all space lines

def exists(str,istr):
    ans=str.find(istr)
    return ans     # use str.find(istr) to return 0 based index of the matched substring, else -1

def titleIt(str):
    ans=str.title()
    return ans      # use str.title() to capitalize the first letter

def casesSwap(str):
    ans=str.swapcase()
    return ans     # use str.swapcase() to swap the cases of lower to upper and upper to lower


def main():
    t=int(input())
    while(t>0):
        str=input()
        s=input()
        str=trim(str)

        print(str)
        print(exists(str,s))
        print(titleIt(str))
        print(casesSwap(str))

        t-=1
if  __name__=='main':
    main()