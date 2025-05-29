todo_list = []
while True:
  if not todo_list:
    print("Your ToDo list is empty")
  else:
    index = 1
    for task in todo_list:
      print(f"{index}. {task}")
      index += 1
  print("Options: ")
  print("1) Add Task")
  print("2) Remove Task")
  print("3) Quit")
  choice = input("Choosed option: ")
  if choice == "1":
    print("Adding task")
    new_task = input("Enter the task: ")
    todo_list.append(new_task)
    print("the task has been added to the todo list")
  elif choice == "2":
    if not todo_list:
      print("Your ToDo list is empty")
    else:
      print("Removing task")
      todo_list.pop(-1)

  elif choice == "3":
    print("Quitting")
    break
