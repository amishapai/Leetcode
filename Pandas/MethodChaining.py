import pandas as pd
l=[]
def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    result_df = animals[animals['weight'] > 100].sort_values(by='weight', ascending=False)[['name']]
    return(result_df)
