"""
Strip leading 0s and count till 0 comes again, return number of steps to reach 1 

""" 
count=0
r=[]
def func1(c):
    global r
    global count
    if c in r:
        return
    else:
        r.append(c)
        c=c+1
        c=str(c)
        c=c.rstrip('0')
        c=int(c)
        count=count+1
        func1(c)
      
      
n=int(input())
count=0
func1(n)
print(count)