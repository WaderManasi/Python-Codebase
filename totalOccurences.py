#You are given a string str, you need to print True 
# if cat and hat appear same number of times in str, 
# otherwise print False.

def cat_hat(str):
  #string.count("substring")  return total occurences
  hat=str.count("hat")
  cat=str.count("cat")
  
  if hat==cat:
     return "True"
  else:
     return "False"

def main():
    t=int(input())
    while(t>0):
        str=input()
        print(cat_hat(str))
        print()
        t-=1
if  __name__=='main':
    main()