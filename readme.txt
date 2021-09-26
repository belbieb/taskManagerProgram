The program is created for a small business to help manage tasks assigned to each member of the team. 
This program will work with two text files, user.txt and tasks.txt .

Open each of the files that accompany this project and take note of the following:
# tasks.txt stores a list of all the tasks that the team is working on.
The data for each task is stored on a separate line in the text file.
Each line includes the following data about a task in this order:
        ■ The username of the person to whom the task is assigned.
        ■ The title of the task.
        ■ A description of the task.
        ■ The date that the task was assigned to the user.
        ■ The due date for the task.
        ■ Either a ‘Yes’ or ‘No’ value that specifies if the task has been
        completed yet.

# user.txt stores the username and password for each user that has permission to use 
the program (task_manager.py). 

The username and password for each user is written into this file in the following format:
        ■ First, the username followed by a comma, a space and then the password.
        ■ One username and corresponding password per line.

The program allows the users to do the following:
* Login. The user is prompted to enter a username and password. 
* A list of valid usernames and passwords are stored in a text file called user.txt . 
* Display an appropriate error message if the user enters a username that is not listed in user.txt or enters a valid
  username but not a valid password. The user should repeatedly be asked to enter a valid username and password until they provide
  appropriate credentials.

The following menu is displayed once the user has successfully logged in:
* Please select one of the following options:
  r - register user
  a - add task  
  va - view all tasks
  vm - view my tasks
  e - exit

USING FUNCTIONS (to improve the modularity of the code):

#If the user chooses ‘r’ to register a user, the user is prompted for a new username and password. 
The user is also be asked to confirm the password. 
If the value entered to confirm the password matches the value of the password, the username
and password should be written to user.txt in the appropriate format.

#If the user chooses ‘a’ to add a task, the user is prompted to enter the username of the person the task is assigned to, 
the title of the task, a description of the task and the due date of the task. 
The data about the new task is written to tasks.txt . 
The date on which the task is assigned is the current date. 
The assumptions is that whenever a user adds
a new task, the value that indicates whether the task has been completed or not is ‘No’.

#If the user chooses ‘va’ to view all tasks, display the information for
each task on the screen in an easy to read format.

# If the user chooses ‘vm’ to view the tasks that are assigned to them,
only display all the tasks that have been assigned to the user that is
currently logged-in in a user-friendly, easy to read manner.

# If the user chooses ‘e’  the  program terminates.