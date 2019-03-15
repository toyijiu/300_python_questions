#use date lib,
import datetime
def dayofyear():
    year = int(input('input the year:'))
    month = int(input('input the month:'))
    day = int(input('input the day:'))
    now = datetime.date(year=year,month=month,day=day)
    first_day = datetime.date(year=year,month=1,day=1)
    return (now-first_day).days+1

if __name__ == '__main__':
    print(dayofyear())