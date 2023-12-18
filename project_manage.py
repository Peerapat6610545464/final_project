# import database module
"""the module use to manage project"""
import csv
import datetime
import sys
from database import Read, DB, Table

# define a funcion called initializing
db = DB()
read = Read()
RESPONSE = "waiting"
RESPONSE_DATE = "-"
FILE_PERSON = db.search("person")
FILE_LOGIN = db.search("login")
FILE_PROJECT = db.search("project")
FILE_ADVISOR = db.search("advisor_pending_request")
FILE_MEMBER = db.search("member_pending_request")
FILE_EVA = db.search("evaluation")

def initializing():
    """to initializing the program and create an object to read all csv files
    that will serve as a persistent state for this program"""
    login_ = read.csv_reader("login.csv")
    person = read.csv_reader("persons.csv")
    project = read.csv_reader("project.csv")
    advisor_pending_request = read.csv_reader("advisor_pending_request.csv")
    member_pending_request = read.csv_reader("member_pending_request.csv")
    evaluation = read.csv_reader("evaluation.csv")
    person_table = Table("person", person)
    login_table = Table("login", login_)
    project_table = Table("project", project)
    advisor_pending_request_table = Table("advisor_pending_request",
                                          advisor_pending_request)
    member_pending_request_table = Table("member_pending_request",
                                         member_pending_request)
    evaluation_table = Table("evaluation", evaluation)
    db.insert(person_table)
    db.insert(login_table)
    db.insert(project_table)
    db.insert(advisor_pending_request_table)
    db.insert(member_pending_request_table)
    db.insert(evaluation_table)


# here are things to do in this function:

# create an object to read all csv files that will serve as a persistent state for this program

# create all the corresponding tables for those csv files

# see the guide how many tables are needed

# add all these tables to the database


# define a funcion called login


def exit_():
    """to save change of the program"""
    with open('login.csv', 'w', newline='') as login:
        file__ = csv.writer(login)
        file__.writerow(['ID', 'username', 'password', 'role'])
        for index in db.search('login').table:
            file__.writerow(index.values())
        login.close()
    with open('persons.csv', 'w', newline='') as persons:
        file__ = csv.writer(persons)
        file__.writerow(['ID', 'first', 'last', 'type'])
        for index in db.search('person').table:
            file__.writerow(index.values())
        persons.close()
    with open('project.csv', 'w', newline='') as project:
        file__ = csv.writer(project)
        file__.writerow(['ID', 'title', 'lead', 'member1'
                            , 'member2', 'advisor',
                         'status', 'project_information'])
        for index in db.search('project').table:
            file__.writerow(index.values())
        project.close()
    with open('advisor_pending_request.csv', 'w', newline='') as advisor_:
        file__ = csv.writer(advisor_)
        file__.writerow(['ID', 'title' 'to_be_advisor_name',
                         'response', 'response_date'])
        for index in db.search('advisor_pending_request').table:
            file__.writerow(index.values())
        advisor_.close()
    with open('member_pending_request.csv', 'w', newline='') as member:
        file__ = csv.writer(member)
        file__.writerow(['ID', 'title', 'to_be_member_name',
                         'response', 'response_date'])
        for index in db.search('member_pending_request').table:
            file__.writerow(index.values())
        member.close()
    with open('evaluation.csv', 'w', newline='') as evaluation:
        file__ = csv.writer(evaluation)
        file__.writerow(['ID', 'title', 'to_evaluate',
                         'response', 'response_date'])
        for index in db.search('evaluation').table:
            file__.writerow(index.values())
        member.close()


class Log:
    """this class is for user to log in"""

    def __init__(self):
        """get username and passwod"""
        print("-----LOGIN TABLE-----")
        self._username = input("Username: ")
        self._password = input("Password: ")

    def log(self):
        """log in"""
        login_1 = db.search('login')
        for index in login_1.table:
            if self._username == index['username'] and \
                    self._password == index['password']:
                print(f"Your log in as {index['role']}")
                return [index['ID'], index['role']]

    @property
    def username(self):
        """return username"""
        return self._username

    # here are things to do in this function:
    # add code that performs a login task
    # ask a user for a username and password
    # returns [ID, role] if valid, otherwise returning None

    # define a function called exit


# here are things to do in this function: write out all the tables that have
# been modified to the corresponding csv files By now, you know how to read
# in a csv file and transform it into a list of dictionaries. For this
# project, you also need to know how to do the reverse, i.e., writing out to
# a csv file given a list of dictionaries. See the link below for a tutorial
# on how to do this:

# https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above


initializing()

while True:
    value = Log()
    val = value.log()
    if val is not None:
        break
    print("Wrong password or username try again")


def delete_line(file_delete_, file_delete_number_):
    """delete line """
    file__ = db.search(f'{file_delete_}').table
    del file__[file_delete_number_ - 2]


def add_line(get_file, value_):
    """add line"""
    file__ = db.search(f'{get_file}')
    if get_file == "login":
        key = {'ID': value_[0], 'username': value_[1], 'password': value_[2],
               'role': value_[3]}
        file__.insert(key)
    if get_file == "persons":
        key = {'ID': value_[0], 'first': value_[1],
               'last': value_[2], 'type': value_[4]}
        file__.insert(key)
    if get_file == "project":
        key = {'ID': value_[0], 'title': value_[1],
               'lead': value_[2], 'member1': value_[3],
               'member2': value_[4], "advisor": value_[5],
               "status": value_[6], "project_information": value_[7]}
        file__.insert(key)
    if get_file == "member_pending_request":
        key = {'ID': value_[0], 'to_be_member': value_[1],
               'response': value_[2], 'response_date': value_[3], }
        file__.insert(key)
    if get_file == "advisor_pending_request":
        key = {'ID': value_[0], 'to_be_advisor': value_[1],
               'response': value_[2], 'response_date': value_[3], }
        file__.insert(key)
    if get_file == "evaluation":
        key = {'ID': value_[0], 'to_evaluate': value_[1],
               'response': value_[2], 'response_date': value_[3], }
        file__.insert(key)


# based on the return value for login, activate the code that performs
# activities according to the role defined for that person_id
while True:
    if val[1] == 'admin':
        print("---------------------")
        print("1.Add any file information")
        print("2.Delete any file information")
        print("3.See any file information")
        print("4.Update any status")
        choice = input("Task number(q to update or quit): ")
        if choice == "q":
            break
        if choice == "1":
            file_add = input("File: ")
            if file_add == "persons":
                ID = input("ID: ")
                first = input("first name: ")
                last = input("last name: ")
                type_ = input("type: ")
                add_line(file_add, [ID, first, last, type_])
            if file_add == "login":
                ID = input("ID: ")
                first = input("username: ")
                last = input("password: ")
                type_ = input("Role: ")
                add_line(file_add, [ID, first, last, type_])
            if file_add == "project":
                ID = input("ProjectID: ")
                title = input("Title: ")
                lead = input("Lead: ")
                member1 = input("Member1: ")
                member2 = input("Member1: ")
                advisor = input("Advisor: ")
                status = input("Status: ")
                info = input("project information: ")
                add_line(file_add,
                         [ID, title, lead, member1,
                          member2, advisor, status, info])
            if file_add == "member_pending_request":
                projectID = input("ProjectID: ")
                title = input("title: ")
                Name = input("Name: ")
                add_line(file_add, [projectID, Name,
                                    RESPONSE, RESPONSE, RESPONSE_DATE, ])
            if file_add == "advisor_pending_request":
                projectID = input("ProjectID: ")
                title = input("title: ")
                Name = input("Name: ")
                add_line(file_add, [projectID, Name,
                                    RESPONSE, RESPONSE, RESPONSE_DATE, ])
            if file_add == "evaluation":
                projectID = input("ProjectID: ")
                title = input("title: ")
                Name = input("Name: ")
                add_line(file_add, [projectID, Name,
                                    RESPONSE, RESPONSE, RESPONSE_DATE, ])
            print("File has been added!!")
        if choice == "2":
            file_delete = input("File: ")
            file_delete_number = int(input("Line: "))
            delete_line(file_delete, file_delete_number)
        if choice == "3":
            file_to_see = input("File: ")
            file = db.search(file_to_see).table
            print(f"{file_to_see} in formation")
            for i in file:
                print(i)
        if choice == "4":
            file_ = input("File to change status: ")
            ID = input("ID to change status: ")
            role = input("Status to change: ")
            role2 = input(f"change {role} to: ")
            file = db.search(f"{file_}")
            file.update(ID, role, role2)
            print(f"{ID} {role} has been change to {role2}!!")
    if val[1] == 'student':
        print("---------------------")
        print("1.See member pending request: ")
        print("2.accepted or deny member pending request: ")
        print("3.Become a lead")
        choice = input("Task number(q to update or quit): ")
        if choice == "q":
            break
        if choice == "1":
            print("member pending request:")
            COUNT = 1
            for i in FILE_MEMBER.table:
                print(f"{COUNT}. {i}")
                COUNT += 1
        if choice == "2":
            answer = input("accept request ID or deny: ")
            COUNT = 1
            for i in FILE_MEMBER.table:
                if i['ID'] == answer:
                    COUNT += 1
                    delete_line("member_pending_request", COUNT)
                    add_line("member_pending_request",
                             [answer, value.username, "accept",
                              datetime.datetime.today()])
                    print(
                        f"you have accepted to be "
                        f"member of group {answer}")
                elif answer == "deny":
                    COUNT += 1
                    delete_line("member_pending_request", COUNT)
                    add_line("member_pending_request",
                             [answer, value.username, "deny",
                              datetime.datetime.today()])
        if choice == "3":
            FILE_LOGIN.update(val[0], 'role', 'lead')
            print("You have been promoted to lead!!")
    if val[1] == 'member':
        print("---------------------")
        print("1.See project status: ")
        print("2.modify project information: ")
        print("3.See who has responded to the requests sent out")
        print("4.Create evaluation request")
        choice = input("Task number(q to update or quit): ")
        if choice == "q":
            break
        if choice == "1":
            COUNT = 1
            for i in FILE_PROJECT.table:
                if value.username in (i['member1'], i['member2']):
                    print(f"{COUNT}. {i}")
                    COUNT += 1
        if choice == "2":
            info = input("Project information ID: ")
            for i in FILE_PROJECT.table:
                if value.username in (i['member1'], i['member2']):
                    FILE_PROJECT.update(i['ID'], "project_information", info)
        if choice == "3":
            print("member_pending_request: ")
            for i in FILE_MEMBER.table:
                print(i)
            print("---------------------")
            print("advisor_pending_request: ")
            for i in FILE_ADVISOR.table:
                print(i)
        if choice == "4":
            projectID = input("ProjectID: ")
            title = input("title: ")
            Name = input("Name: ")
            add_line("evaluation", [projectID, Name,
                                    RESPONSE, RESPONSE, RESPONSE_DATE, ])
    if val[1] == 'lead':
        print("---------------------")
        print("1.See project status: ")
        print("2.modify project information: ")
        print("3.See who has responded to the requests sent out")
        print("4.Send out requests to potential members")
        print("5.Send out requests to a potential advisor")
        print("6.Create evaluation request")
        choice = input("Task number(q to update or quit): ")
        if choice == "q":
            break
        if choice == "1":
            COUNT = 1
            for i in FILE_PROJECT.table:
                if value.username in (i['member1'], i['member2']):
                    print(f"{COUNT}. {i}")
                    COUNT += 1
        if choice == "2":
            info = input("Project information ID: ")
            for i in FILE_PROJECT.table:
                if value.username in (i['member1'], i['member2']):
                    FILE_PROJECT.update(i['ID'], "project_information", info)
        if choice == "3":
            print("member_pending_request: ")
            for i in FILE_MEMBER.table:
                print(i)
            print("---------------------")
            print("advisor_pending_request: ")
            for i in FILE_ADVISOR.table:
                print(i)
        if choice == "4":
            print("Create member request:")
            ProjectID = input("ProjectID: ")
            Name = input("Name: ")
            add_line("member_pending_request", [ProjectID, Name,
                                                RESPONSE, RESPONSE,
                                                RESPONSE_DATE, ])
        if choice == "5":
            print("Create advisor request:")
            ProjectID = input("ProjectID: ")
            Name = input("Name: ")
            add_line("advisor_pending_request", [ProjectID, Name,
                                                 RESPONSE, RESPONSE,
                                                 RESPONSE_DATE, ])
        if choice == "6":
            projectID = input("ProjectID: ")
            title = input("title: ")
            Name = input("Name: ")
            add_line("evaluation", [projectID, Name,
                                    RESPONSE, RESPONSE, RESPONSE_DATE, ])
    if val[1] == 'faculty':
        print("---------------------")
        print("1.See project status: ")
        print("2.accepted or deny advisor pending request: ")
        choice = input("Task number(q to update or quit): ")
        if choice == "q":
            break
        if choice == "1":
            COUNT = 1
            for i in FILE_PROJECT.table:
                if value.username in (i['member1'], i['member2']):
                    print(f"{COUNT}. {i}")
                    COUNT += 1
        if choice == "2":
            answer = input("accept request ID or deny: ")
            COUNT = 1
            for i in FILE_PROJECT.table:
                if i['ID'] == answer:
                    COUNT += 1
                    delete_line("advisor_pending_request", COUNT)
                    add_line("advisor_pending_request",
                             [answer, value.username, "accept",
                              datetime.datetime.today()])
                    print(
                        f"you have accepted to be "
                        f"advisor of group {answer}")
                elif answer == "deny":
                    COUNT += 1
                    delete_line("advisor_pending_request", COUNT)
                    add_line("advisor_pending_request",
                             [answer, value.username, "deny",
                              datetime.datetime.today()])
    if val[1] == 'advisor':
        print("---------------------")
        print("1.See project status: ")
        print("2.See pending request: ")
        print("3.Send out requests to a potential evaluation ")
        print("4.accept or deny evaluation request")
        choice = input("Task number(q to update or quit): ")
        if choice == "q":
            break
        if choice == "1":
            COUNT = 1
            for i in FILE_PROJECT.table:
                if value.username in (i['member1'], i['member2']):
                    print(f"{COUNT}. {i}")
                    COUNT += 1

        if choice == "3":
            projectID = input("ProjectID: ")
            title = input("title: ")
            Name = input("Name: ")
            add_line("evaluation", [projectID, Name,
                                    RESPONSE, RESPONSE, RESPONSE_DATE, ])

        if choice == "4":
            answer = input("accept request ID or deny: ")
            COUNT = 1
            for i in FILE_EVA.table:
                if i['ID'] == answer:
                    COUNT += 1
                    delete_line("evaluation", COUNT)
                    add_line("evaluation",
                             [answer, value.username, "accept",
                              datetime.datetime.today()])
                elif answer == "deny":
                    COUNT += 1
                    delete_line("evaluation", COUNT)
                    add_line("evaluation",
                             [answer, value.username, "deny",
                              datetime.datetime.today()])

# if val[1] = 'admin':
# see and do admin related activities
# elif val[1] = 'student':
# see and do student related activities
# elif val[1] = 'member':
# see and do member related activities
# elif val[1] = 'lead':
# see and do lead related activities
# elif val[1] = 'faculty':
# see and do faculty related activities
# elif val[1] = 'advisor':
# see and do advisor related activities

# once everyhthing is done, make a call to the exit function
exit_()
