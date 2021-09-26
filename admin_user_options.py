from task_manager_add_task import *
from task_manager_view_all import *
from task_manager_view_mine import *
import datetime
import math
from collections import Counter

def exit_options():
     print('>>> EXITING PROGRAMME <<<')

def admin_user_options(username,option_input):
    if username=="admin" and option_input == "gr":
        
        create_file_taskViewer = open("task_overview.txt","w+")
        with open("tasks.txt", "r") as tf:
         file_contents = tf.readlines()
         count = 0
         for line in file_contents:
            count += 1
        create_file_taskViewer.write("Total Number of Tasks in Task File: {}".format(count))

        with open("tasks.txt","r") as stf:
             line_count = 0
             yes_count = 0
             no_count = 0
             file_read = stf.readlines()
             for line in file_read:
              line_list = file_read[line_count].strip().split(",")
              line_count+=1
              if "No" in line: 
                    no_count += 1    
              if "Yes" in line: 
                    yes_count += 1
        create_file_taskViewer.write("\nTotal Tasks Completed: {}".format(yes_count))
        create_file_taskViewer.write("\nCurrent Number of Incomplete Tasks: {}".format(no_count))


        today = datetime.datetime.today()
        with open("tasks.txt","r") as f:
           due_count = 0
           overdue_count = 0
           file_re = f.readlines()
           for line in file_re:
                line_list = file_re[due_count].strip().split(",")
                due_count+=1  
                if line_list[4] == str(today):
                    overdue_count += 1          
        create_file_taskViewer.write("\nTotal Overdue Tasks: {}".format(overdue_count))
        
        incomplete_percent = (no_count/count)*100
        overdue_percent = math.floor((overdue_count/count)*100)
        create_file_taskViewer.write("\nPercentage of Tasks Incomplete: {}".format(incomplete_percent))
        create_file_taskViewer.write("\nPercentage of Tasks Overdue: {}".format(overdue_percent))
        create_file_taskViewer.close()

                                                          
        create_file_userViewer = open("user_overview.txt","w+")
        with open("user.txt", "r") as f:
            user_count = 0
            for line in f:
                user_count += 1
        create_file_userViewer.write("Total Number of Registered Users: {}".format(user_count))
        with open("tasks.txt", "r") as tas:
         q = tas.readlines()
        count = 0
        for line in q:
            count += 1
        create_file_userViewer.write("\nTotal Number of Tasks in Task File: {}\n************************".format(count))
       
        with open("tasks.txt", "r") as f:
            users_in_file = []
            in_file = f.readlines()
            for line in in_file:
                name = line.strip().split(",")[0]
                users_in_file.append(name)
                occur =dict(Counter(users_in_file))
        for user,tasks in occur.items():            
            create_file_userViewer.write("\nTotal Number of Tasks Assigned to {}: {}".format(user,tasks))
            percent_assignedto_user = math.floor((tasks/count)*100)
            create_file_userViewer.write("\nPercentage of Tasks Assigned to {}: {}%\n*************************".format(user, percent_assignedto_user))
            
         
        
        with open("tasks.txt","r") as f:
            complete_count = []
            not_complete_count = []
            file = f.readlines()
            for line in file:
                name_user = line.split(',')[0]
                if "No" in line:
                    not_complete_count.append(name_user)
                    counting_no_names =dict(Counter(not_complete_count))
                if "Yes" in line:
                    complete_count.append(name_user)
                    counting_yes_names =dict(Counter(complete_count))     
        for yes_name,yes in counting_yes_names.items(): 
            create_file_userViewer.write("\nTasks Completed by {}: {}".format(yes_name,yes))
            percent_yes = math.floor((yes/count)*100)
            create_file_userViewer.write("\nPercentage of Tasks Completed by {}: {}%\n~~~~~~~~~~~~~~~~".format(yes_name, percent_yes))
        for no_name,no in counting_no_names.items(): 
            create_file_userViewer.write("\nTasks still to be completed by {}: {}".format(no_name, no))
            percent_no = math.floor((no/count)*100)
            create_file_userViewer.write("\nPercentage of Tasks still to be completed by {}: {}%\n~~~~~~~~~~~~~~~~".format(no_name, percent_no))

   
    elif username == 'admin'and option_input == "t":
        if option_input == 't':
            tasks_file = open('tasks.txt', 'r')
            num_tasks = len(tasks_file.readlines())
            print("Total number of tasks is: " + str(num_tasks))
            tasks_file.close()
    elif username == 'admin'and option_input == 'u':
            users_file = open('user.txt', 'r')
            num_users = len(users_file.readlines())
            print("Total number of users is: " + str(num_users))
            users_file.close()



    
    elif username == "admin" and option_input == "r":
        user_file = open('user.txt', 'r')
        reading_user_file = user_file.read()
        print("You are the admin, with rights to register users.")
        
        username = input("Please enter the username you want to register first:\n")

        if username in reading_user_file:
            while username in reading_user_file:
                username = input("Username already exists.\nPlease enter the username you want to register first:\n")

        password = input("Enter the user's password:\n")
        password_confirmation = input("Please confirm the password by typing it again:\n")
        while password != password_confirmation:
            print("Your confirmation password is not a match.") 
            password = input("Enter the user's password:\n")
            password_confirmation = input("Please confirm the password by typing it again:\n")
        
        if password == password_confirmation:
            print("New User has been registered!")
            user_file = open('user.txt', 'a+')
            user_file.write('\n'+ username + ',')

            user_file.write(password)
            user_file.close()
          
    elif username != "admin" and option_input == "r":
            print("You can add a task but can't register new users.")
           
       




def reading_task_file():
        tasks_file = open('tasks.txt', 'r')
        reading_tasks_file = tasks_file.read()
        
