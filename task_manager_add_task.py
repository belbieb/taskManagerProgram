import datetime
from dateutil import parser
#above is the appropriate modules and other imports.


"""If the user chooses ‘a’ to add a task, the user should be prompted to
enter the username of the person the task is assigned to, the title of
the task, a description of the task and the due date of the task. The
data about the new task should be written to tasks.txt . The date on
which the task is assigned should be the current date. Also assume
that whenever you add a new task, the value that indicates
whether the task has been completed or not is ‘No’."""


def add_task(option_input):
    if option_input == "a":
        username_task = input("Please enter the username of the person the task will be assigned to:\n")
        task_title = input("Please enter the title of the task:\n")
        task_description = input("Please enter the description of the task:\n")
        assignment_date = str(datetime.datetime.now().strftime("%d " + "%B " + "%Y"))
        due_date_task =(input("Please enter the due date of the task:\n"))
        task_complete = "No"
        tasks_file = open('tasks.txt', 'a+')
        line_entry = "\n" + username_task + ", "+ task_title + ", "+ task_description + ", "+ assignment_date + ", "+ due_date_task + ", "+ task_complete
        tasks_file.write(line_entry)
        print("Entry complete.")
        tasks_file.close()



"""If the user selects a specific task, they should be able to choose to
either mark the task as complete or edit the task . If the user
chooses to mark a task as complete, the ‘Yes’/’No’ value that
describes whether the task has been completed or not should be
changed to ‘Yes’. When the user chooses to edit a task, the username of the person to whom 
the task is assigned or the due date of the task can be edited. 
The task can only be edited if it has not yet been completed."""

def edit_username(username,username_change,sentence):
    tasks_file = open('tasks.txt', 'r+')
    readin_file = tasks_file.readlines()
    for line in readin_file:
        
            names_in_file = line.split(',')[0]
           
            if names_in_file == username and sentence == line:
                position_line = readin_file.index(sentence)
                username_replaced = line.replace(names_in_file,username_change)
                open_file_Mode = open('tasks.txt','w')   
                readin_file[position_line] = username_replaced       
                open_file_Mode.writelines(readin_file)
                print("Username was updated!")


def edit_due_date(username,change_due_date,line):
    tasks_file = open('tasks.txt', 'r+')
    readin_file = tasks_file.readlines()
    if line in readin_file:
        if username ==line.split(',')[0]:
            position_line = readin_file.index(line)
            current_due_date = line.split(', ')[4]
            due_date_replaced = line.replace(current_due_date,change_due_date)
            open_file_Mode = open('tasks.txt','w')   
            readin_file[position_line] = due_date_replaced 
            open_file_Mode.writelines(readin_file)
            print("The DUE DATE was updated!")
          
