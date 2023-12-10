import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    j=0
    k=0
    for i in players.columns:
        j+=1
    for i in players.values:
        k+=1
    return([k,j])
