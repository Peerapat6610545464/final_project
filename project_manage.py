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
    username = input("Username: ")
    password = input("Password: ")
    login_1 = db.search('login')
    for i in login_1.table:
        if username == i['username'] and password == i['password']:
            return [i['ID'], i['role']]

    # print(login_1.table)


# here are things to do in this function:
# add code that performs a login task
# ask a user for a username and password
# returns [ID, role] if valid, otherwise returning None
def convert_csv(name, data):
    # file = open(f"{name}.csv", 'w')
    # writer = csv.writer(file)
    # for i in data[0].keys():
    #     writer.writerow(i)
    # for i in data.values():
    #
    #     writer.writerow(i)
    # file.close()
    pass


# define a function called exit
def exit():
    # for i in db.database:
    #     table_data = db.search(i.table_name)
    #     convert_csv(i.table_name, table_data.table)
    pass

# here are things to do in this function:
# write out all the tables that have been modified to the corresponding csv files
# By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:

# https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above

initializing()
val = login()

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

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
