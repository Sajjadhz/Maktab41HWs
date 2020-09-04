# In the Name of Allah, the Most Beneficent, the Most Merciful
# Sajjad_Hosseinzadeh_HW3_Maktab41
# This Python file includes weekday_generator and Hanoi_tower functions

from datetime import datetime, timedelta

# Part 1
def weekday_generator(start_date, end_date, week_day):
    D1 = datetime.fromisoformat(start_date)
    D2 = datetime.fromisoformat(end_date)
    number_of_weeks = (D2 - D1).days//7 # get the number of weeks in given interval
    for i in range(number_of_weeks):
        requested_day = D1 + timedelta(days = i * 7 + week_day - 1)# go forward to the i'th week and given days
        yield datetime.strftime(requested_day,'%d %B %Y')
        

# please uncomment the following lines to run test cases
'''
my_weekday = weekday_generator("2020-02-18", "2020-05-02", 3)
print(next(my_weekday))
print(next(my_weekday))
print(next(my_weekday))
'''

# Part 2
def Hanoi_tower(start, middle, goal, n):    
    if n == 1:       
        print(start + " -> " + goal)# just print the movement.
        return
    elif n > 1:        
        Hanoi_tower(start, goal, middle, n - 1 )# move n - 1 disks from source rod to middle rod.
        Hanoi_tower(start, middle, goal, 1)# move 1 disk from source rod to target rod.
        Hanoi_tower(middle, start, goal, n - 1)# move n - 1 disks from middle rod to target rod.

# please remove the comment mark to run the test case
# Hanoi_tower("A", "B", "C", 3)
