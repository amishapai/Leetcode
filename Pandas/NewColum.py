import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    bon=[]
    for i in employees['salary']:
        bon.append(i*2)
    employees["bonus"]=bon
    return(employees)
