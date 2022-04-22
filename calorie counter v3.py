#First, we import date and time functions that will read the computer's
#current date and time. We define how we want our time and date to appear.
from datetime import date, time, datetime
date_time = datetime.now()
minimized_date = str(date_time.month) + "-" + str(date_time.day) + "-" + str(date_time.year)
minimized_time = str(date_time.hour) + ":" + str(date_time.minute)
minimized_date_time = str(minimized_date) + ", " + str(minimized_time)

#Our logs, in the form of lists. 
#First, a log simply of all calorie int values, that we can use to add 
#all the calories ate together and keep a running total. 
#Second, a list comprised of each complete calorie entry, so we can later have all our entries
#displayed.
#Both start at 0 so we can sum each time another calorie value is added.
cals_logged_val = []
cals_logged_datetime = []


#The function asking the user to input their calories eaten just now, and
#then storing the quantity with its date and time in variables.
def cal_in():
    ate = input('How many calories did you just eat? ')
    cal_val = int(ate)
    full_log_entry = str(cal_val) + 'cal' + "  (" + minimized_date_time + ")"
#Now, the integer value of the calories ate is added to the list of cals_logged_val.
#And the interger value with date and time are added to list of cals_logged_datetime.
    cals_logged_val.append(cal_val)
    cals_logged_datetime.append(full_log_entry)
    return full_log_entry

#Now, the running total of cals is calculated by summing the elements of the list
#before the next iteration of the function runs. I could have also
def running_total_cals():
    total_cals = 0
    for n in cals_logged_val:
        total_cals = total_cals + n
    return total_cals
        
#Now we actually invoke the function, and then tell the computer to keep
#running the function indefinitely, so the user can keep logging calories 
#as much as they want.
while True:
    cal_in()
    running_total_cals()
    print(cal_in())
    print(cals_logged_val)
    print(cals_logged_datetime)
    print(running_total_cals())
    
    









