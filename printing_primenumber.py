def is_prime(num):
    t=True
    f=False
    if num>1:
        i=2
        # prime=True
        while i<num:
            result=num%i
            # i+=1
            if result==0:
                status=f
                break
            if i==num-1:
                if result!=0:
                    status=t
                    break
            i+=1
    if num==2:
        status=t
        

    return status

# y=int(input("Enter any number:" ))

# result=is_prime(y)
# print(result)


# Write your code here.
#

for i in range(1, 100):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
