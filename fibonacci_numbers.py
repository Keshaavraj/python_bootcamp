def fib(n):
    if n<1:
        return None
    if n<3:
        return 1
        
    
    x1=x2=1
    x3=x1+x2
    
    for x in range(3, n+1):
        x3=x1+x2
        x1,x2=x2,x3
    
    return x3

for i in range(1,8):
    result=fib(i)
    print(result)

x=int(input("Enter the number: "))
result=fib(x)
print(result)




        