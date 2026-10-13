tasks = []
while True:
    print('menu: [1]view tasks [2]add task [3]leave')
    choice = input("select a choice ")
if choice == 1:
    print('menu:')
    for i,tasks in enumerate(tasks,1):
        print(f"{i}. {task}")
    if not tasks:
        print('no tasks added')
elif choice == '2':
    item = input("Enter task name: ")
    tasks.append(item)
    print(f"successfully added {item}")
elif choice == 3:
    print("Goodbye")
    

