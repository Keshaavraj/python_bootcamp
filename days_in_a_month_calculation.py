def days_in_month(year, month):
    
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
    
    if x==True:
        if month==2:
            days=29
        elif (month in [1,3,5,7,8,10,12]):
            days=31
        elif (month in [4,6,9,11]):
            days=30
    elif x==False:
        if month==2:
            days=28
        elif (month in [1,3,5,7,8,10,12]):
            days=31
        elif (month in [4,6,9,11]):
            days=30
    return days
        
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
