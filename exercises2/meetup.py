
from datetime import date
# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.
 
    message: explanation of the error.
 
    """
    def __init__(self, message):
        self.message = message
d_o_w_dict = {
     1 : "Monday",
     2 : "Tuesday",
     3 : "Wednesday",
     4 : "Thursday",
     5 : "Friday",
     6 : "Saturday",
     7 : "Sunday",
    }
def meetup(year, month, week, day_of_week):
    days_in_month = (date(year+(month)//12, month%12 + 1, 1)-date(year,month,1)).days
    weekday_in_month = [d_o_w_dict[date(year, month, i).isoweekday()] \
                        for i in range(1,days_in_month+1)]
    if week == "teenth":
        day = 13 + weekday_in_month[12:19].index(day_of_week)
    elif week == "last":
        day = len(weekday_in_month) - weekday_in_month[::-1].index(day_of_week)
    else:
        day_first = weekday_in_month.index(day_of_week)+1
        day_second = weekday_in_month.index(day_of_week,day_first)+1
        day_third = weekday_in_month.index(day_of_week,day_second)+1
        day_fourth = weekday_in_month.index(day_of_week,day_third)+1
        day_fifth = weekday_in_month.index(day_of_week,day_fourth)+1 \
            if weekday_in_month.count(day_of_week) > 4 else 0
        if week == "first" or week =="1st":
            day = day_first 
        elif week == "second" or week =="2nd":
            day = day_second
        elif week == "third" or week =="3rd":
            day = day_third
        elif week == "fourth" or week =="4th":
            day = day_fourth
        elif day_fifth:
            day = day_fifth
        else:
            raise MeetupDayException("That day does not exist.")
            
    return date(year,month,day)