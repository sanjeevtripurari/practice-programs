# Task Manager with User Authentication
# Course-End Project Problem Statement

import os
import getpass
import cryptocode
import json

from datetime import datetime
import time

def mencrypt(mstring):
    passkey = '\a' 
    cipher = cryptocode.encrypt(mstring,passkey)
    return cipher

def mdecrpyt(mcipher):
    string=cryptocode.decrypt(mcipher,'\a')
    return string

def check_user(user_name):
    for user in users:
        if mdecrpyt(user['name'])==user_name:
            return True
    else:
        return False

def check_registeration():
    logged_in=False
    global current_user
    
    print("\n## Registration ##\n")
    are_you=input("Are you registered user? (y/n): ")
    
    if are_you.lower()=='y':
        user_name=input("\nEnter username: ")
        for user in users:
            if mdecrpyt(user['name'])==user_name:
                user_pass = getpass.getpass('Password:')
                if mdecrpyt(user['pass'])==user_pass:
                    print(f"\nUser: {user_name} successfully logged in..\n")
                    current_user=user
                    logged_in=True
                    ud=int(time.time())
                    user['updatetm']=ud
                else:
                    print("\nInvalid password, please try again..\n")
    else:
        print("\nUser Registration\n ")
        user={}
        user_name=input("\nEnter username: ")
        if user_name=="":
            print("\nNo username entered exiting..\n")
            exit(1)
   
        while check_user(user_name):
            print("username already exists.. enter different username")
            user_name=input("Enter username: ")
            if user_name=="":
                print("No username entered exiting")
                exit(1)
                
        user_Full_name=input("Enter fullname: ")
        user_email_id=input("Enter email id: ")                
        user_pass1=getpass.getpass(prompt='Enter password: ')
        user_pass2=getpass.getpass(prompt='Enter password again: ')
        
        if user_pass1==user_pass2:
            user['name']=mencrypt(user_name)
            user['pass']=mencrypt(user_pass1)
            user['email']=user_email_id
            user['createtm']=int(time.time())
            user['updatetm']=int(time.time())
            users.append(user)
            register_file = 'register.fil'
            with open(register_file, "a+") as f:
                f.write("{}:{}:{}:{}:{}\n".format(user['email'],user['name'],user['pass'],user['createtm'],user['updatetm']))
            print(f"\nUser:{user_name} added successfully and logged in.\n")
            current_user=user
            logged_in=True
    return logged_in


def store_task_file():
    task_file = "usertasks.json"
    with open(task_file, 'w+') as file:
            json.dump(usertasks, file, ensure_ascii=False)


def load_task_file():
    current_email=current_user['email']
    current_ctm=current_user['createtm']
    global usertasks
    task_file = "usertasks.json"
    if os.path.exists(task_file):
        mode='r'
    else:
        mode='w+'     
        
    with open(task_file, mode) as file:
        if mode=='r':
            usertasks=json.load(file)    
        else:
            user_json='{"usertasks":[]}'
            json.dump(user_json, file, ensure_ascii=False)
            usertasks=json.loads(user_json) 
            
def load_registeration():
    register_file = 'register.fil'
    if os.path.exists(register_file):
        mode='r'
    else:
        return     
        
    with open(register_file, mode) as f:
        reg_readline=f.read()
        
    for u in reg_readline.splitlines():
            user={}
            user['email'],user['name'],user['pass'],user['createtm'],user['updatetm']=u.strip().split(':')
            users.append(user)
            

def view_tasks(user_mail, usertasks):
    tasks=[]
    for user in usertasks['usertasks']:
        if user['mail'] == user_mail:
            tasks=user['tasks']
    if tasks:
        print("\nTaskID\tStatus  \tDescription\n")
        for tasklist in tasks:
            for k,v in tasklist.items():
                print(f"{v}  \t", end="")
            print()
        print("\n")
        v=input("\nView the Task List..\nPress ENTER key to continue\n")
        return True

    else:
        print(f"\nNo tasks found for {user_mail}\n")
        return False
    
    v=input("")
    
def add_tasks(user_mail, usertasks):
    v_status=view_tasks(user_mail, usertasks)
    a_taskitem={}
    a_taskId=input("Enter task id to Add: ")
    a_taskDescription=input("Enter task description: ")
    a_taskitem["taskid"]=a_taskId
    a_taskitem["status"]="pending"
    a_taskitem["detail"]=a_taskDescription    
    for usertask in usertasks['usertasks']:
        if usertask['mail'] == user_mail:
            usertask['tasks'].append(a_taskitem)
            break
    else:
        usertasks['usertasks'].append({"mail": user_mail, "tasks": [a_taskitem]})

    store_task_file()
    v=input(f"\nAdded TaskID: {a_taskId}\nPress ENTER key to continue\n")
    return True

    
def delete_task(user_mail, usertasks):
    v_status=view_tasks(user_mail, usertasks)
    delete_task=False
    d_taskId=input("Enter task id to delete: ")
    for usertask in usertasks['usertasks']:
        if usertask['mail'] == user_mail:
            usertask['tasks'] = [task for task in usertask['tasks'] if task['taskid'] != d_taskId]
            delete_task=True
            break
    if delete_task:
        store_task_file()
        v=input(f"\nDeleted TaskID: {d_taskId}\nPress ENTER key to continue\n")
        return True

def modify_task(user_mail, usertasks):
    v_status=view_tasks(user_mail, usertasks)
    a_taskitem={}
    updated_task=False
    a_taskId=input("Enter task id to mark completed: ")
    updated_task={"status": "completed"}
    for usertask in usertasks['usertasks']:
        if usertask['mail'] == user_mail:
            for task in usertask['tasks']:
                if task['taskid'] == a_taskId:
                    task['status']="completed"
                    updated_task=True
                    break
    if updated_task:
        store_task_file()
        v=input(f"\nUpdated TaskID: {a_taskId} as completed\nPress ENTER key to continue\n")
        return True

## main program

users=[]
current_user={}
usertasks={}

load_registeration()
if not check_registeration():
    print("\nNo login found exiting..\n")
    exit(1)

load_task_file()

while True:
        
    print(f"""

    ##  Task Management System - {current_user['email']} ##
    
    1.. Add a Task
    2.. View Tasks
    3.. Mark a Task as Completed
    4.. Delete a Task

    5.. Logout

        """)

    choice=int(input("Enter your choice: "))

    if choice==1:
        print(f"\n## Add a Task - {current_user['email']} ##\n")
        add_tasks(current_user['email'], usertasks)
    elif choice==2:
        print(f"\n## View Tasks - {current_user['email']} ##\n")
        v_status=view_tasks(current_user['email'], usertasks)
    elif choice==3:
        print(f"\n## Mark a Task as Complete - {current_user['email']} ###\n")
        modify_task(current_user['email'], usertasks)
    elif choice==4:
        print(f"\n## Delete a Task - {current_user['email']} ##\n")
        delete_task(current_user['email'], usertasks)
    elif choice==5:
        print(f"\n## Logout - {current_user['email']} ##\n")
        break
    else:
        print("\nInvalid choice try again..\n")  
        
        
# Done.