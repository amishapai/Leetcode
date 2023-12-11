import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students = students.dropna(subset=['name'])
    #student=pd.DataFrame()
    #student=students.copy()
    #todrop = students[students['name'] = 'null'].index
    #student.drop(student[student.name == 'null'].index, inplace= True)
    #students.drop(todrop , inplace=True)
    return(students)
