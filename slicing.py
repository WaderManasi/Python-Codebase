# Given a string of braces named bound_by,
# and a string named tag_name. The task is to print a new string such that tag_name is in the middle of bound_by. For example, bound_by : "<<>>" 
# and tag_name : "body", so, new string should be ""<

def join_middle(bound_by, tag_name):
    c=len(bound_by)/2
    c=int(c)
  # complete the statement below to return the string as required
    return bound_by[0:c] + tag_name + bound_by[c:]

def main():
    t=int(input())
    while(t>0):
        string=input()
        string1=string[0]
        string2=string[1]
        print(join_middle(string1,string2))
        
        t-=1

if  __name__=='main':
    main()