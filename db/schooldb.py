import sqlite3 as sql
schooldb = sql.connect('C:\\python-calisma\\python-calisma\\db\\schooldb.db')

imlec = schooldb.cursor()

crate_table_string = '''\
    CREATE TABLE IF NOT EXISTS Student (\
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
            student_number INTEGER,\
                name TEXT,\
                    surname TEXT,\
                        birth_date TEXT,\
                            gender INTEGER)'''

imlec.execute(crate_table_string)

schooldb.commit()
schooldb.close()


class Student:
    def __init__(self,student_number,name,surname,birth_date,gender):
        self.student_number = student_number
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.gender = gender


def kayit_yap(student):
    schooldb = sql.connect('C:\\python-calisma\\python-calisma\\db\\schooldb.db')
    imlec = schooldb.cursor()
    imlec.execute(f'''INSERT INTO Student (student_number,name,surname,birth_date,gender) VALUES ({student.student_number},"{student.name}","{student.surname}","{student.birth_date}",{student.gender})''')

    schooldb.commit()
    schooldb.close()

student = Student(212,"aykut","bayraktar","29-01-1989",1)
student = Student(211,"ömer","bayraktar","18-11-2018",1)

kayit_yap(student)


