

FINE_YEAR = 10_000
FINE_MONTH = 500
FINE_DAY = 15


day,month,year = map(int, input().split())
day_e,month_e,year_e = map(int, input().split())

#case year is greater than year expected
if year > year_e:
    fine = FINE_YEAR
    print(fine)
#case same year but different months
elif year == year_e:
    if month > month_e:
        fine = (month-month_e)*FINE_MONTH
        print(fine)
#case same year,same month but different days
    else:
        if day >day_e:
            fine = (day-day_e)*FINE_DAY
            print(fine)
    #case same year same month dates less than or equals to
        else:
            fine = 0
            print(fine)
#case year under expected
else:
    fine = 0
    print(fine)
