from math import e
from task_manager_add_task import *
from task_manager_view_all import *
from task_manager_view_mine import *
from admin_user_options import*
#above is the appropriate modules and other imports.

def exit_options():
    print('>>> EXITING PROGRAMME <<<')

"""Your program should allow your users to do the following:
Login. The user should be prompted to enter a username and
password. A list of valid usernames and passwords are stored in a
text file called user.txt . Display an appropriate error message if the
user enters a username that is not listed in user.txt or enters a valid
username but not a valid password. The user should repeatedly be
asked to enter a valid username and password until they provide
appropriate credentials."""
user_file = open('user.txt', 'r')
reading_user_file = user_file.readlines()


navigate = True
while navigate:
    # The user is prompted to enter a username and a password.
    username = input("Please enter your username:\n")
    password = input("Enter your password:\n")
    for line in reading_user_file:
        users_list = line.split(",")
        if username != users_list[0] and password == users_list[1].strip("\n"):
            print("Are you sure you are registered, because your username is not recognized. Do you want to try again?\n")
        elif username == users_list[0] and password != users_list[1].strip("\n"):
            print("Sorry that password is incorrect. Do you want to try again?\n")

        elif username == users_list[0] and password == users_list[1].strip("\n"):
            print('Welcome ' + username + '!\n'+"You have logged in with the right details!")
            navigate = False

        

            if username == "admin":
                print("Please select one of the following options:\nr -register user\na -add task\nva -view all tasks\nvm -view my tasks\ngr -generate reports\nDISPLAY STATISTICS:\nt = DISPLAY -> total number of tasks.\nu = DISPLAY -> total number of users.\ne -exit")
            else:
                 print("Please select one of the following options:\nr -register user\na -add task\nva -view all tasks\nvm -view my tasks\ne -exit")
            option_input = input("Please enter your option:\n")
            while option_input != "e":
                admin_user_options(username,option_input)
                add_task(option_input)
                view_all(option_input)
                view_mine(option_input,username)
                if username == "admin":
                    print("Please select one of the following options:\nr -register user\na -add task\nva -view all tasks\nvm -view my tasks\ngr -generate reports\nDISPLAY STATISTICS:\nt = DISPLAY -> total number of tasks.\nu = DISPLAY -> total number of users.\ne -exit")
                else:
                   print("Please select one of the following options:\nr -register user\na -add task\nva -view all tasks\nvm -view my tasks\ne -exit")
                   option_input = input("Please enter your option:\n")
            
user_file.close()

