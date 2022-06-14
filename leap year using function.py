def is_year_leap(year):
    c=True
    f=False
    if (year%4==0 and year%100!=0):
        x=c
    elif(year%400!=0 and year%100==0):
        x=f
    elif(year%400==0):
        x=c
    elif(year%100==0):
        x=c
    else:
        x=f
    return x


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
