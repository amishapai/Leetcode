import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df=pd.DataFrame()
    a=[]
    b=[]
    for i in range (0, len(student_data)):
        a.append(student_data[i][0])
        b.append(student_data[i][1])
    df = df.assign(student_id=a, age=b)
    return(df)
