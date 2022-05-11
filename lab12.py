"""last one on 5-4-22"""
import sqlite3


class Gradebook():
    def __init__(self):
        """
        We create connect to the :memory: database and
        create a cursor which we set to a private variable
        for use in other methods
        """
        connection = sqlite3.connect(":memory:")
        self.__database = connection.cursor()
        self.__database.execute("CREATE TABLE gradebook(student, grade)")
        print("database has been created")

    def upload_grade(self):
        """
        Your INSERT statements
        """
        grade_list = [
            ('Amy', 81),
            ('Bob', 65),
            ('Kim', 94),
            ('Sam', 55),
        ]
        self.__database.executemany("INSERT INTO gradebook VALUES (?,?)", grade_list)
        self.__database.commit()

    def student_grade(self):
        """
        Your SELECT Statement
        """
        self.__database.execute("SELECT grade FROM gradebook WHERE student=:student",
                                {"student": Amy})
        print(cur.fetchall())
        for row in self.__database.execute('SELECT * FROM gradebook ORDER BY grade'):
            print(row)
        self.__database.close()


def test_Gradebook():
    """
    1) Initalize GradeBook
    2) Insert some grades
    3) Get back a single users grade
    """


def __init__Gradebook(self, student, grade):
    grade = 75
    assert grade >= 0
    assert grade <= 100


def test_upload_grade():
    assert grade >= 0


def test_grade():
    grade = 32
    assert grade >= 0
    assert grade <= 100


def main():
    test_Gradebook()
    test_grade()


if __name__ == "__gradebook__":
    gradebook()



