import pandas as pd
import numpy as np
from etl import *

def test_transform_adds_age_after_5_yrs():
    df = pd.DataFrame({"id": [1, 2], "name": ["Andy", "Billy"], "age": [10, 40]})
    df_out = transform_add_age(df)

    assert "age_after_5_yrs" in df_out.columns
    assert list(df_out["age_after_5_yrs"]) == [15, 45]

def test_transform_add_unique_col():
    df = pd.DataFrame({"id": [1, 2], "name": ["Andy", "Billy"], "age": [10, 40],"age_after_5_yrs":[15,45]}) 
    df_out=transform_add_unique_col(df)

    assert "unique_col" in df_out.columns
    assert list(df_out["unique_col"])==["A1","B2"]

def test_transform_check_age_bracket():
    df = pd.DataFrame({"id": [1, 2], "name": ["Andy", "Billy"], "age": [10, 40]}) 
    df_out=transform_add_age_bracket(df)  

    assert "age_bracket" in df_out.columns
    assert list(df_out["age_bracket"])==["junior","senior"] 

    
