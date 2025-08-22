from  datetime import datetime

user_input = input("enter your goal with deadline separated by a colon ex: learn python:10.02.20024\n")
input_list = user_input.split(":")
print(input_list)
goal = input_list[0]
deadline = input_list[1]

try:
    deadline_date = datetime.strptime(deadline,"%d.%m.%Y")
    today_date = datetime.today()

    # calculating how many days from now till deadline
    remaining_days = deadline_date - today_date
    remaining_minutes = remaining_days.seconds/60
    remaining_hours = remaining_minutes/60
    print(f"Remaining days : {remaining_days.days} days to reach your goal: {goal}\nRemaining Hours: {remaining_hours} h\n")
except ValueError:
    print("Enter the correct format")






