def view_all(option_input):
    """If the user chooses ‘va’ to view all tasks, display the information for
        each task on the screen in an easy to read format."""
    if option_input == "va":
        tasks_file = open('tasks.txt', 'r')
        list_tasks = tasks_file.read()
        print("List of the tasks is:\n--------------------\n",list_tasks)
        tasks_file.close()

