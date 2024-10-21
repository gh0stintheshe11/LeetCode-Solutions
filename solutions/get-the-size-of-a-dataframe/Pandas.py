import pandas as pd
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    # Use the shape attribute to get the number of rows and columns
    return [players.shape[0], players.shape[1]]