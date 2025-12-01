from etl import *
import pandas as pd

def test_extract_returns_df():
    engine = get_engine()
    df_out=extract(engine)

    assert isinstance(df_out,pd.DataFrame)
    for col in ["id","name","age"]:
        assert col in df_out.columns

