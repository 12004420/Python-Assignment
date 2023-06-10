
from datetime import datetime, timedelta

def check_date_difference(from_date, to_date, difference):
 
    from_date_obj = datetime.strptime(from_date, '%y-%m-%d')
    to_date_obj = datetime.strptime(to_date, '%y-%m-%d')
    date_difference = to_date_obj-from_date_obj
    
    if date_difference < timedelta(days=difference):
        return True
    else:
        return False
from_date=input("Enter a string representing a date in the form of yy-mm-dd :-> ")
to_date =input("Enter a string representing a date in the form of yy-mm-dd :->")
difference=int(input("Enter a difference"))
print(check_date_difference(from_date,to_date,difference))
