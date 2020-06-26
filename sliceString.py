#Given two strings a and b.
#The task is to make a new string where the string with longer length should be in between and the one with shorter length should be outside on front and end.
#New string should be like shorter+longer+shorter.

def combo_string(a, b):
  l1=int(len(a))
  l2=int(len(b))
  
  if(l1>l2):
      short=b
      longer=a
  else:
      short=a
      longer=b
      
  
  return short+longer+short

def main():
    t=int(input())
    while(t>0):
        string=input()
        string1=string[0]
        string2=string[1]
        print(combo_string(string1,string2))
        
        t-=1

if  __name__=='main':
    main()