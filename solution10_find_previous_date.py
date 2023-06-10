   
from datetime import datetime, timedelta

def get_date(date, n):
    
    date_obj = datetime.strptime(date, '%y-%m-%d')
    delta = timedelta(days=n)
    previous_date = date_obj - delta
    previous_date_str = previous_date.strftime('%y-%m-%d')
    return previous_date_str
    
a=input("Write a date in the form of yy-mm-dd ")
n=int(input("Enter a  number you want to subtract from given date "))
result=get_date(a,n)
print("after subtracting :->", result)
