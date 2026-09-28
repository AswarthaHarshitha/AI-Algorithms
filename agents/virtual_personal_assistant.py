import datetime

task_list = []
meet_list = []

def add_task(task):
    task_list.append(task)
    print("Added:", task)

def show_tasks():
    print("Tasks:")
    for task in task_list:
        print(task)

def add_meet(date, time, note):
    meet_list.append(f"{date} {time} - {note}")
    print("Added:", date, time, note)

def show_meets():
    print("Meetings:")
    for meet in meet_list:
        print(meet)

def now():
    print("Now:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))


add_task("Read")
show_tasks()

add_meet("2025-02-10", "14:00", "Doctor")
show_meets()

now()
