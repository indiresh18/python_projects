print("====DO TO LIST====")
list=[]
def display():
    print("1.SEE OUR LIST")
    print("2.ADD A TASK")
    print("3.DELETE A TASK")
    print("4.EXIT")
    print("SELECT AN OPERATION")

def traverse():
    print(list)
def add():
    task=input("ENTER A TASK")
    list.append(task)
    print("ADDED SUCCESSULLY")

def delete():
    print("which task need to be deleted:")
    for i in range(len(list)):
        print(i+1,".",list[i])
    index=int(input("SELECT WHICH ONE TO DELETE"))
    removed=list.pop(index-1)
    print("Removed the task:",removed)
    
        
    
while True:
    display()
    choice=int(input("Enter an operation:"))
    if choice==1:
        traverse()
    elif choice==2:
        add()
    elif choice==3:
        delete()
    else:
        print("THANKS FOR USING THIS DO TO LIST")
        break

    