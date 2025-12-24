import datetime
import jdatetime #Terminal: python -m pip install jdatetime

def gregorian_to_jalali(year, month, day):
    g_date = datetime.date(year, month, day)
    j_date = jdatetime.date.fromgregorian(date=g_date)
    return j_date

def get_today_jalali():
    today  = datetime.date.today()
    return gregorian_to_jalali(today.year, today.month, today.day)

# print(get_today_jalali())
print(gregorian_to_jalali(2025, 11, 19))