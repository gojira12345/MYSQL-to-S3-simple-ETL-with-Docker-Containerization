import os
import boto3
import json
from botocore.exceptions import ClientError

DB_HOST=os.getenv("DB_HOST")
DB_PORT=int(os.getenv("DB_PORT","3306"))
DB_USER=os.getenv("DB_USER")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_NAME=os.getenv("DB_NAME")

S3_ENDPOINT=os.getenv("S3_ENDPOINT")
S3_ACCESS_KEY=os.getenv("S3_ACCESS_KEY")
S3_SECRET_KEY=os.getenv("S3_SECRET_KEY")
DB_SECRET_NAME=os.getenv("DB_SECRET_NAME")

def get_db_credentials():
    secret_name = DB_SECRET_NAME
    print("DEBUG DB_SECRET_NAME:", secret_name)

    if secret_name:
        try:
            client = boto3.client("secretsmanager")
            response = client.get_secret_value(SecretId=secret_name)
            secret = json.loads(response["SecretString"])
            print("DEBUG using secret host:", secret.get("host"))
            return {
                "host": secret["host"],
                "port": int(secret["port"]),
                "user": secret["username"],
                "password": secret["password"],
                "dbname": secret["dbname"],
            }
        except (ClientError, KeyError, json.JSONDecodeError) as e:
            print("DEBUG secret error, falling back to env:", repr(e))

    print("DEBUG using env host:", DB_HOST)
    return {
        "host": DB_HOST,
        "port": DB_PORT,
        "user": DB_USER,
        "password": DB_PASSWORD,
        "dbname": DB_NAME,
    }
