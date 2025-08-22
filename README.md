# 🐍Module 13 – Programming with Python
This exercise is part of Module 13: Programming with Python, module introduces Python programming fundamentals through three hands-on demo projects. Each demo focuses on solving a different type of problem: a countdown application, automation with spreadsheets, and interacting with an external API.

# 📦Demo 1 – Write a Countdown Application
# 📌 Objective
Develop a Python application that accepts a user-defined goal and deadline, then calculates and displays the remaining time until the deadline.

# 🚀 Technologies Used
* Python: programming language.
* IntelliJ- PyCharm: IDE used for development.
  
# 🎯 Features
✅Installing Python.
✅Accepts user input for goal and deadline.
⏳Calculates time remaining until deadline.
🖥️Displays a countdown in the console.

# 🏗 Project Architecture

# ⚙️ Project Configuration
1. Install Python locally on your machine, following the steps according to your OS.
   
   [Python](https://www.python.org/downloads/release/python-3137/)
   ```bash
     apt update
     apt install python3
     python3 --version
   ```
   
2. Install PyCharm following the steps according to your OS.
   [PyCharm](https://www.jetbrains.com/help/pycharm/installation-guide.html)
   
3. Import the datetime module.
   
   ```bash
   from datetime import datetime
   ```
   
4. Request the desired goal and deadline for the goal from the user.
   
   ```bash
     user_input = input("enter your goal with deadline separated by a colon ex: learn python:10.02.20024\n")
   ```
  
5. Save the input to a list variable to identify the goal and the deadline.
   
   ```bash
       input_list = user_input.split(":")
       print(input_list)
       goal = input_list[0]
       deadline = input_list[1]
   ```
   
6. Convert the input deadline to a date format.
   
   ```bash
   deadline_date = datetime.strptime(deadline,"%d.%m.%Y")
   ```
   
7. Check Today's date
   
   ```bash
   today_date = datetime.today()
   ```
8. Calculate remaining days until deadline
   
   ```bash
      remaining_days = deadline_date - today_date
      remaining_minutes = remaining_days.seconds/60
      remaining_hours = remaining_minutes/60
      print(f"Remaining days : {remaining_days.days} days to reach your goal: {goal}\nRemaining Hours: {remaining_hours} h\n")
   ```
