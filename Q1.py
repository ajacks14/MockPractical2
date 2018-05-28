#q1a
def fib(n):
    if n <=1:
        return n
    else:
        return fib(n-1) + fib(n-2)
#
# for x in range(20):
#     print(fib(x),end=" ")
#



#q1b
counter=0
breaks=False
n=0
exit=0
while not breaks:
   exit=fib(n)
   if exit >=2000:
       breaks=True
   if exit<=2000:
       print(fib(n),end=" ")
       n+=1
       counter+=1

print("There were {} terms".format(counter))

