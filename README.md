# Final project for 2023's 219114/115 Programming I
* how to use this program
  - login with username and password
  - the program will show you what option is available
  - example: if the  program ask for file write "file" do not wire "file.csv"
  - example2: if the program ask for "accept request ID or deny: " if you want 
    to accept write ID of the project or userid foe deny just write "deny"
  - write q to quit
* python file 
  - **database.py**
    -    to manage data
          `class Table` (list of dictionaries)
          `class DB` (list of table)
          class Read` (read any csv file)
  - **project_manage.py**
    -     main part of the program
          start the program and receive user inout
          program that take user input and to the task user request
    -    `def initializing` (use class Table, DB, Read to store data)
    -    `class Log` (user log in)
    -    `def exit_` (to exit the program and update the change in data)
  * csv file
    - **login.csv**
    -     log in information
          ID,username,password,role
    - **person.csv**
    -     person information
          ID,first,last,type
    - **project.csv**
    -     project information
          ID,title,lead,member1,member2,advisor,status,project_information
    - **advisor_pending_request.csv**
    -     aadvisor_pending_request
          ID,to_be_advisorr,response,response_date
    - **member_pending_request.csv**
    -     member_pending_request
          ID,to_be_member,response,response_date
  * bug
    -     sometime random "[]" appear in member or advisor csv file
          only change status in login.csv
    * role
      - **student**
      -     1.See member pending request
            2.accepted or deny member pending request
            3.Become a lead
      - - **lead**
      -     1.See project status
            2.modify project information
            3.See who has responded to the requests sent out
            4.Send out requests to potential members
            5.Send out requests to a potential advisor
      - - **member**
      -     1.See project status
            2.modify project information
            3.See who has responded to the requests sent out
      - - **faculty**
      -     1.See project status
            2.accepted or deny advisor pending request
      -  **advisor**
      -     1.See project status
            2.See pending request
            3.Send out requests to a potential evaluation 
            4.accept or deny evaluation request
      - **admin**
      -     1.Add any file information
            2.Delete any file information
            3.See any file information
            4.Update any status

# Table detailing each role and its actions

| Role    | Action                                         | Method                 | Class   | Completion |
|---------|------------------------------------------------|------------------------|---------|------------|
| admin   | Add any file information                       | add_line               | admin   | 100%       |
| admin   | Delete any file information                    | delete_line            | admin   | 100%       |
| admin   | See any file information                       | search                 | admin   | 100%       |
| admin   | Update any status                              | update                 | admin   | 100%       |
| student | See member pending request                     | input                  | student | 100%       |
| student | accepted or deny member pending request        | add_line, delete_line  | student | 100%       |
| student | Become a lead                                  | add_line, delete_line  | student | 100%       |
| member  | See project status                             | search                 | student | 100%       |
| member  | See and Modified project information           | add_line, delete_line  | student | 100%       |
| member  | See who has responded to the requests sent out | search                 | student | 100%       |
| lead    | See project status                             | search                 | lead    | 100%       |
| lead    | modify project information                     | add_line,d delete_line | lead    | 100%       |
| lead    | See who has responded to the requests sent out | search                 | lead    | 100%       |
| lead    | Send out requests to potential members         | add_line,d delete_line | lead    | 100%       |
| lead    | Send out requests to a potential advisor       | add_line,d delete_line | lead    | 100%       |
| faculty | See project status                             | search                 | faculty | 100%       |
| faculty | accepted or deny advisor pending request       | add_line,d delete_line | faculty | 100%       |
| advisor | See project status                             | search                 | advisor | 100%       |
| advisor | See pending request                            | search                 | advisor | 100%       |
| advisor | Send out requests to a potential evaluation    | add_line,d delete_line | advisor | 100%       |
| advisor | accept or deny evaluation request              | add_line,d delete_line | advisor | 100%       |