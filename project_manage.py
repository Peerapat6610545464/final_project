# import database module
from database import Read, DB, Table
import csv
import datetime

# define a funcion called initializing
db = DB()
read = Read()


def initializing():
    login_ = read.csv_reader("login.csv")
    person = read.csv_reader("persons.csv")
    project = read.csv_reader("project.csv")
    advisor_pending_request = read.csv_reader("advisor_pending_request.csv")
    member_pending_request = read.csv_reader("member_pending_request.csv")
    person_table = Table("person", person)
    login_table = Table("login", login_)
    project_table = Table("project", project)
    advisor_pending_request_table = Table("advisor_pending_request",
                                          advisor_pending_request)
    member_pending_request_table = Table("member_pending_request",
                                         member_pending_request)
    db.insert(person_table)
    db.insert(login_table)
    db.insert(project_table)
    db.insert(advisor_pending_request_table)
    db.insert(member_pending_request_table)


# here are things to do in this function:

# create an object to read all csv files that will serve as a persistent state for this program

# create all the corresponding tables for those csv files

# see the guide how many tables are needed

# add all these tables to the database


# define a funcion called login


def exit():
    with open('login.csv', 'w', newline='') as file1:
        file__ = csv.writer(file1)
        file__.writerow(['ID', 'username', 'password', 'role'])
        for i in db.search('login').table:
            file__.writerow(i.values())

    with open('persons.csv', 'w', newline='') as file2:
        file__ = csv.writer(file2)
        file__.writerow(['ID', 'first', 'last', 'type'])
        for i in db.search('person').table:
            file__.writerow(i.values())

    with open('project.csv', 'w', newline='') as file3:
        file__ = csv.writer(file3)
        file__.writerow(['ProjectID', 'Title', 'Lead', 'Member1'
                            , 'Member2', 'Advisor', 'Status'])
        for i in db.search('project').table:
            file__.writerow(i.values())

    with open('advisor_pending_request.csv', 'w', newline='') as file4:
        file__ = csv.writer(file4)
        file__.writerow(['ProjectID', 'to_be_advisor',
                         'Response', 'Response_date'])
        for i in db.search('advisor_pending_request').table:
            file__.writerow(i.values())

    with open('member_pending_request.csv', 'w', newline='') as file5:
        file__ = csv.writer(file5)
        file__.writerow(['ProjectID', 'to_be_member',
                         'Response', 'Response_date'])
        for i in db.search('member_pending_request').table:
            file__.writerow(i.values())


class Log_in:

    def __init__(self):
        print("-----LOGIN TABLE-----")
        self._username = input("Username: ")
        self._password = input("Password: ")

    def log(self):
        login_1 = db.search('login')
        for i in login_1.table:
            if self._username == i['username'] and \
                    self._password == i['password']:
                print(f"Your log in as {i['role']}")
                return [i['ID'], i['role']]
        # print(login_1.table)

    @property
    def username(self):
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

value = Log_in()
val = value.log()

def delete_line(file_delete_, file_delete_number_):
    file = db.search(f'{file_delete_}').table
    print(file)
    del file[file_delete_number_ - 2]
    print(file)


def add_line(file_, value):
    file = db.search(f'{file_}')
    print(file)
    if file_ == "login":
        key = {'ID': value[0], 'username': value[1], 'password': value[2],
               'role': value[3]}
        file.insert(key)
    if file_ == "persons":
        key = {'ID': value[0], 'first': value[1],
               'last': value[2], 'type': value[4]}
        file.insert(key)
    if file_ == "project":
        key = {'ProjectID': value[0], 'Title': value[1],
               'Lead': value[2], 'Member1': value[3],
               'Member2': value[4], "Advisor": value[5],
               "Status": value[6]}
        file.insert(key)
    if file_ == "member_pending_request":
        key = {'ProjectID': value[0], 'to_be_member': value[1],
               'Response': value[2], 'Response_date': value[3], }
        print(key)
        file.insert(key)

    def answer_request(requestID, status=None):
        pass


# based on the return value for login, activate the code that performs
# activities according to the role defined for that person_id
while True:
    if val[1] == 'admin':
        print("---------------------")
        print("1.Add any file information")
        print("2.Delete any file information")
        print("3.See any file information")
        print("4.Update status")
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
                last = input("passworde: ")
                type_ = input("Role: ")
                add_line(file_add, [ID, first, last, type_])
            if file_add == "project":
                ID = input("ProjectID: ")
                Title = input("Title: ")
                Lead = input("Lead: ")
                Member1 = input("Member1: ")
                Member2 = input("Member1: ")
                Advisor = input("Advisor: ")
                Status = input("Status: ")
                add_line(file_add,
                         [ID, Title, Lead, Member1, Member2, Advisor, Status])
            if file_add == "member_pending_request":
                ProjectID = input("ProjectID: ")
                Title = input("Title: ")
                to_be_member = input("to_be_member: ")
                Response = input("Response: ")
                Response_date = input("Response_date: ")
                add_line(file_add, [ProjectID, Title,
                                    to_be_member, Response, Response_date, ])
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
            file_ = input("File to change status")
            ID = input("ID to change status: ")
            role = input("Status to change")
            role2 = input(f"change {role} to: ")
            file = db.search(f"{file_}")
            file.update(ID, role, role2)
            print(f"{ID} {role} has been change to {role2}!!")

    if val[1] == 'student':
        file = db.search("member_pending_request")
        file_ = db.search("login")
        print("---------------------")
        print("1.See member pending request: ")
        print("2.accepted or deny member pending request: ")
        print("3.Become a lead")
        choice = input("Task number(q to update or quit): ")
        if choice == "q":
            break
        if choice == "1":
            print("member pending request:")
            count = 1
            for i in file.table:
                print(f"{count}. {i}")
                count += 1
        if choice == "2":
            answer = input("accept request ID or deny: ")
            count = 1

            for i in file.table:
                if i['ProjectID'] == answer:
                    count += 1
                    delete_line("member_pending_request", count)
                    add_line("member_pending_request",
                             [answer, value.username, "accept",
                              datetime.datetime.today()])
                    print(f"you have accepted to be member of group {answer}")
        if choice == "3":
            file_.update(val[0], 'role', 'lead')
            print("You have been promoted to lead!!")
    if val[1] == 'member':
        pass
    if val[1] == 'lead':
        pass
    if val[1] == 'faculty':
        pass
    if val[1] == 'advisor':
        pass

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
exit()
