from sqlalchemy import create_engine,text
import pandas as pd
import boto3
import datetime
import io
from config import *


creds=get_db_credentials()
conn_str = f"mysql+pymysql://{creds["user"]}:{creds["password"]}@{creds["host"]}:{creds["port"]}/{creds["dbname"]}"
engine = create_engine(conn_str)

def get_s3_client():
    kwargs={}
    if S3_ENDPOINT:
        kwargs["endpoint_url"]=f"http://{S3_ENDPOINT}"
        kwargs["aws_access_key_id"]=S3_ACCESS_KEY
        kwargs["aws_secret_access_key"]=S3_SECRET_KEY
    return boto3.client("s3",**kwargs)

def get_engine():
    conn_str = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    return create_engine(conn_str)


def extract(engine)-> pd.DataFrame:
    with engine.connect() as conn:
    
         df= pd.read_sql("SELECT * FROM tbl",engine)
         return df
           

def transform_add_age(df:pd.DataFrame)-> pd.DataFrame:
   df_out=df.copy()
   df_out["age_after_5_yrs"]=df_out["age"]+5
   return df_out

def transform_add_unique_col(df:pd.DataFrame)->pd.DataFrame:
   df_out=df.copy() 
   df_out["unique_col"]=df_out["name"].str[0]+df["id"].astype('str')
   return df_out  





def load(df:pd.DataFrame):
    s3 = get_s3_client()
    bucket = "databuckett12345"
    key = "output_tbl.csv"+ str(datetime.datetime.now())
    csv_buf = io.StringIO()
    df.to_csv(csv_buf, index=False)
    s3.put_object(Bucket=bucket, Key=key, Body=csv_buf.getvalue())   



def main():
    engine = get_engine()
    df_extract = extract(engine)
    df_transformed_1 = transform_add_age(df_extract)
    print(df_transformed_1)
    df_transformed_2=transform_add_unique_col(df_transformed_1)
    print(df_transformed_2)
    load(df_transformed_2)

if __name__=="__main__":
    main()    










