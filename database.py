"""this modul is to manage data base"""
# try wrapping the code below that reads a persons.csv file in a class and
# make it more general such that it can read in any csv file

import csv
import os


class Read:
    """to read file"""
    def __init__(self):
        """get location"""
        self.__location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def csv_reader(self, name):
        """read any csv file"""
        list_ = []

        with open(os.path.join(self.__location__, name)) as f:
            rows = csv.DictReader(f)
            for r in rows:
                list_.append(dict(r))
        return list_


# add in code for a Database class
class DB:
    """data base"""
    def __init__(self):
        """set database default"""
        self.database = []

    def insert(self, table):
        """insert table"""
        self.database.append(table)

    def search(self, table_name):
        """search data"""
        for table in self.database:
            if table.table_name == table_name:
                return table
        return None

    def database(self):
        """return data"""
        return self.database


# add in code for a Table class

class Table:
    """table to sore data"""
    def __init__(self, table_name, table):
        """table name and value"""
        self.table_name = table_name
        self.table = table

    def insert(self, other):
        """insert data"""
        self.table += [other]

    def update(self, user_id, key, value, ):
        """update data"""
        for i in self.table:
            if i['ID'] == user_id:
                i[key] = value



# modify the code in the Table class so that it supports the insert
# operation where an entry can be added to a list of dictionary

# modify the code in the Table class so that it supports the update
# operation where an entry's value associated with a key can be updated
