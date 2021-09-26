from math import e
from os import replace
from admin_user_options import*
from task_manager_add_task import *
from task_manager_view_all import *
from admin_user_options import*
#above is the appropriate modules and other imports.


def exit_options():
    """function for exiting the program at any point (it takes no arguments, prints a message)."""
    print('>>> EXITING PROGRAMME <<<')


def view_mine(option_input,username):
    """If the user chooses ‘vm’ to view the tasks that are assigned to them,
only display all the tasks that have been assigned to the user that is
currently logged-in in a user-friendly, easy to read manner."""
    if option_input == "vm": 
        with open ('tasks.txt', 'r') as tasks_file:
            line_read = tasks_file.read()
            if username not in line_read:
                print("There's no tasks with your name!") 
            else: 
                count = 0
                dict_content = {}
                tasks_file = open('tasks.txt', 'r') 
                for line in tasks_file:
                    names_in_file = line.split(',')[0]
                    count += 1
                    if username ==names_in_file:
                        dict_content[str(count)] = line
                        print("Task number = " + str(count))
                        print("Assigned to:" + line.split(',')[0])
                        print("Task Title:" + line.split(',')[1])
                        print("Task Description:" + line.split(',')[2])
                        print("Date assigned:" + line.split(',')[3])
                        print("Due date:" + line.split(',')[4])
                        print("Task complete?:" + line.split(',')[5])
                print("**************************************************")
                main_menu = input('Please enter a [-1] to return to the main menu or select the task number for edits:\n')
                if main_menu in dict_content.keys():
                    print(dict_content.get(main_menu))
                    task_complete_or_edit = input("Please select one of the following options:\nc - mark the task as complete\ned -edit the task\n")
                    if task_complete_or_edit == 'c':
                        tasks_file = open('tasks.txt', 'r+') 
                        read_file = tasks_file.readlines()
                        pure_line =dict_content.get(main_menu)
                        position_line = read_file.index(pure_line)
                        word_replacement=read_file[position_line].replace("No","Yes")
                        open_file_writeMode = open('tasks.txt','w')      
                        read_file[position_line] = word_replacement 
                        open_file_writeMode.writelines(read_file)
                        print("TASK DETAILS UPDATED!") 
                        
                   
                    elif task_complete_or_edit == 'ed': 
                        tasks_file = open('tasks.txt', 'r+') 
                        read_file = tasks_file.readlines()
                        pure_line =dict_content.get(main_menu)
                        if "No" in pure_line:
                            edit_option = input("Enter (00) > Edit Username.\nEnter (01) > Edit Date.\n")
                            if edit_option == '00':
                                username_change = input("Please enter the new username you wish to reassign the task to:\n")
                               
                                edit_username(username,username_change,dict_content.get(main_menu))
                           
                            if edit_option =='01':
                                    due_date_change = input("Please enter the new due date:\n")
                                    edit_due_date(username,due_date_change,dict_content.get(main_menu))
                        else:
                            print("SORRY: This Task Cannot be Edited, because it's COMPLETE!")   
                elif main_menu == '-1':
                    if username == "admin":
                            print("Please select one of the following options:\nr -register user\na -add task\nva -view all tasks\nvm -view my tasks\ngr -generate reports\nds -display statistics\nt = DISPLAY -> total number of tasks.\nu = DISPLAY -> total number of users.\ne -exit")
                    else:
                        print("Please select one of the following options:\nr -register user\na -add task\nva -view all tasks\nvm -view my tasks\ne -exit")
                        option_input = input("Please enter your option:\n")
                         
                        tasks_file.close()
                        
                    
                
                        
                    
                    
                                
