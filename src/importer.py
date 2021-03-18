import pandas as pd
from pathlib import Path

#load the csv file from anywhere and load it into a dataframe
def load_file(filename: str) -> pd.DataFrame:
    path = Path(__file__).resolve().parents[1]
    file = Path(path, filename)
    df = pd.read_csv(file)
    return df