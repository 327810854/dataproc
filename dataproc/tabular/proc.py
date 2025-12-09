import pandas as pd
from pathlib import Path
from typing import List, Optional

def load_csv(path: str, **kwargs) -> pd.DataFrame:
    """
    Load a CSV file and return a pandas DataFrame.
    """
    return pd.read_csv(path, **kwargs)

def save_csv(df: pd.DataFrame, out_path: str, index: bool = False) -> None:
    """
    Save a pandas DataFrame to CSV. Create parent folder if necessary.
    """
    Path(out_path).parent.mkdir(parents=True, exist_ok=True) 
    df.to_csv(out_path, index=index)

def drop_empty(df: pd.DataFrame, how: str = 'any') -> pd.DataFrame:
    """
    Drop rows that have empty cells.
    how: 'any' (drop if any NaN in the row) or 'all' (drop only if all NaN).
    """
    return df.dropna(axis=0, how=how)

def fill_empty(df: pd.DataFrame, value=None, method: Optional[str]=None) -> pd.DataFrame:
    """
    Fill empty cells either with a constant value or with method 'ffill'/'bfill'.
    If method is provided, it will be used and value is ignored.
    """
    if method:
        return df.fillna(method=method)
    else:
        return df.fillna(value)
def drop_duplicates(df: pd.DataFrame, subset: Optional[List[str]] = None) -> pd.DataFrame:
    """
    Remove duplicate rows and keep only one row for each duplicate group.
    
    Parameters:
    - subset: list of columns to check for duplicates.
              If None, all columns are used.
              
    Keeps the first occurrence and removes the rest.
    """
    return df.drop_duplicates(subset=subset, keep='first')

def keep_columns(df, columns):
    """
    Keep only the provided list of columns.
    Raises KeyError if any requested column is missing.
    """
    return df[columns]