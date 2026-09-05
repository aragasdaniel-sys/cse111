"""A time calculator program designed to help the user understand how they are spending their time
Author: Daniel Aragão"""

import csv
from datetime import datetime, timedelta

def log_entry(filename, activity_data, time_data):
    """Writes data on the csv file"""

    date = datetime.now()
    now = date.strftime("%a %B %d %Y")
    with open(filename, "at", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        combined_row = [now, activity_data, time_data]
        writer.writerow(combined_row)

def read_csv_file(filename):
    """Reads the csv file"""

    with open(filename, "rt", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file, fieldnames=["date", "activity", "hours"])
        rows = []
        for row in reader:
            rows.append(row)
    return rows

def filter_time(entries):
    """Filters the list for the most recent entries"""

    today = datetime.now()
    recent_entries = []

    for entry in entries:
        entry_date = datetime.strptime(entry["date"], "%a %B %d %Y")
        difference = today - entry_date
        if difference.days <= 7:
            recent_entries.append(entry)
    return recent_entries

def display_goal(filename):
    """Returns the goal found on the goal file"""
    with open(filename, "rt") as goal_file:
        goal = int(goal_file.read())
    return goal

def set_goal(filename, goal):
    """Updates goals"""
    with open(filename, "wt") as goal_file:
        goal_file.write(str(goal))
    return goal

def calculate_percentage(stu_hours, goal):
    """Calculates the percentage of studied hours"""

    try:
        percentage = (stu_hours/(goal*7)) * 100
        return percentage

    except ZeroDivisionError as zero_div:
        print("Goal cannot be 0")
        return 0

def display_weekly_report(filtered_list):
    """Sums the studied hours for display, 
    calling the calculate_percentage function also for display."""

    total_hours = 0
    for row in filtered_list:
        hours = int(row["hours"])
        total_hours += hours
    
    goal = display_goal("goal.txt")
    print(f"You studied a total of {total_hours} hours")
    percentage = calculate_percentage(total_hours, goal)
    if percentage > 0:
        print(f"That's about {round(percentage)}% of your weekly goal")

def main():
    """Displays main menu to the user in loop. 
    Calls functions depending on the user's input."""
    try:
        display_goal("goal.txt")
    except FileNotFoundError:
        set_goal("goal.txt", 0)
    while True:
        print()
        print("Welcome to Study Tracker")
        print("Press:")
        print("1 for a new log")
        print("2 to view weekly report")
        print("3 to view/change a goal")
        print("0 to quit the program")
        decision = input("Type: ")

        if decision == "1":
            activity_data = input("What did you study? ")
            time_data = input("For how many hours? ")
            log_entry("log.csv", activity_data, time_data)

        elif decision == "2":
            file_list = read_csv_file("log.csv")
            filtered_list = filter_time(file_list)
            display_weekly_report(filtered_list)

        elif decision == "3":
            view_update = int(input("Would you like to view(1) the goal or to update(2) it? "))
            if view_update == 1:
                display = display_goal("goal.txt")
                print(f"Your goal is {display}")

            else:
                new_goal = input("How many hours do you want to study daily? ")
                goal = set_goal("goal.txt", new_goal) 

        else:
            break

if __name__ == "__main__":
    main()