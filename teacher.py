startSalary=int(input("Enter beginning salary : "))
per=2/100
years=list(range(1,(int(input("Enter no of years : "))+1)))
def cal(startSalary,per,years):
    for year in years:
        salin=startSalary*per
        newSal=startSalary+salin
        startSalary=newSal
        print("Year",year," : ",newSal)
cal(startSalary,per,years)
