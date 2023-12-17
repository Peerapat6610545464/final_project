# import database module
from database import Read, DB, Table
import csv

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
    member_pending_request_table = Table("member_pending_request_table",
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

def login():
    print("-----LOGIN TABLE-----")
    username = input("Username: ")
    password = input("Password: ")
    login_1 = db.search('login')
    for i in login_1.table:
        if username == i['username'] and password == i['password']:
            print(f"Your log in as {i['role']}")
            print("----------------------")
            return [i['ID'], i['role']]
    # print(login_1.table)


# here are things to do in this function:
# add code that performs a login task
# ask a user for a username and password
# returns [ID, role] if valid, otherwise returning None


# define a function called exit
def exit():
    with open('login.csv', 'w', newline='') as file:
        file = csv.writer(file)
        file.writerow(['ID', 'username', 'password', 'role'])
        for i in db.search('login').table:
            file.writerow(i.values())

    with open('persons.csv', 'w', newline='') as file:
        file = csv.writer(file)
        file.writerow(['ID', 'first', 'last', 'type'])
        for i in db.search('person').table:
            file.writerow(i.values())

    with open('project.csv', 'w', newline='') as file:
        file = csv.writer(file)
        file.writerow(['ProjectID', 'Title', 'Lead', 'Member1'
                          , 'Member2', 'Advisor', 'Status'])
        for i in db.search('project').table:
            file.writerow(i.values())


# here are things to do in this function: write out all the tables that have
# been modified to the corresponding csv files By now, you know how to read
# in a csv file and transform it into a list of dictionaries. For this
# project, you also need to know how to do the reverse, i.e., writing out to
# a csv file given a list of dictionaries. See the link below for a tutorial
# on how to do this:

# https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above

initializing()
val = login()


def delete_line(file_delete_, file_delete_number_):
    with open(f'{file_delete_}.csv') as file_:
        line = file_.readline()
        print(line)
    # if file_delete_number_ <= len(line):
    #     del line[int(file_delete_number_) - 1]
    #     with open(f'{file_delete_}.csv', 'w', newline='') as f:
    #         for i in line:
    #             file_.write(i)
    # else:
    #     print(f"line {file_delete_number_} not in file")


def add_line(file_, value):
    file = db.search(f'{file_}')
    if file_ == "login":
        key = {'ID': value[0], 'username': value[1], 'password': value[2],
               'role': value[3]}
        file.insert(key)
    if file_ == "persons":
        key = {'ID': value[0], 'first': value[1],
               'last': value[2], 'type': value[4]}
        file.insert(key)
        print(key)
    if file_ == "project":
        key = {'ProjectID': value[0], 'Title': value[1],
               'Lead': value[2], 'Member1': value[3],
               'Member2': value[4], "Advisor": value[5],
               "Status": value[6]}
        print(key)
        file.insert(key)


# based on the return value for login, activate the code that performs
# activities according to the role defined for that person_id
while True:
    if val[1] == 'admin':
        print("---------------------")
        print("1.Add project")
        print("2.Delete project")
        choice = input("Task number(q to quit): ")
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
                first = input("First name: ")
                last = input("Last name: ")
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
            print("File has been added")
        if choice == "2":
            file_delete = input("File: ")
            file_delete_number = int(input("Line: "))
            delete_line(file_delete, file_delete_number)
    if val[1] == 'student':
        pass
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
