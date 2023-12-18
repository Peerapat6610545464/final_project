# Final project for 2023's 219114/115 Programming I
* python file 
  - **database.py**
    - to manage data
    - `class Table` (list of dictionaries)
    - `class DB` (list of table)
    - `class Read` (read any csv file)
  - **project_manage.py**
    - main part of the program
    - start the program and receive user inout
    - program that take user input and to the task user request
    - `def initializing` (use class Table, DB, Read to store data)
    - `class Log` (user log in)
    - `def exit_` (to exit the program and update the change in data)
* role
  - **student**
  -     1.See member pending request
        2.accepted or deny member pending request
        3.Become a lead
  - - **lead**
  -     1.See project status:
        2.modify project information:
        3.See who has responded to the requests sent out
        4.Send out requests to potential members
        5.Send out requests to a potential advisor
  - - **member**
  -     1.See project status: 
        2.modify project information: 
        3.See who has responded to the requests sent out
  - - **faculty**
  -     1.See project status: 
        2.accepted or deny advisor pending request: 
  -  **advisor**
  -     1.See project status: 
        2.See pending request: 
        3.Send out requests to a potential evaluation 
  - **admin**
  -     1.Add any file information
        2.Delete any file information
        3.See any file information
        4.Update any status
* csv file
  - **login.csv**
  - **person.csv**
  - **project.csv**
  - **login.csv**