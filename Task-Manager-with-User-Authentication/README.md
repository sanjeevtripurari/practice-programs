# Task Manager with User Authentication
# Course-End Project Problem Statement

## User Registration

```
## Registration ##

Are you registered user? (y/n): n

User Registration

Enter username: sam
Enter fullname: Sam Bahadur
Enter email id: sam@bahadur.com
Enter password: 
Enter password again:

User:sam added successfully and logged in.
```

## Task Management System

```
    ##  Task Management System - sam@bahadur.com ##

    1.. Add a Task
    2.. View Tasks
    3.. Mark a Task as Completed
    4.. Delete a Task

    5.. Logout



Enter your choice: 5

## Logout - sam@bahadur.com ##
```

## Program description
Program for Task Management System, it requires valid user to login to manage the tasks
- User Registration
  - users are maintained in external file `regiter.fil`, it contains emailid in plain text, username and password in encrypted format
  - file is comma seperated values, and loaded as soon as program is loaded
  - program asks if its already registered user, if yes will take username and cross verify, if file is not there or user then program exits
  - for valid user, it will check username and password then user is successfully validated
- Task Management
  - users tasks are maintained in external file `usertasks.json`, it contains useremail, which is key attribute
  - tasks are added in array, with taskid, status, description
  - default status is always pending
  - user can add task, view task, delete task and mark completed
  