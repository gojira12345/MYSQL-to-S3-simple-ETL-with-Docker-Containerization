import os

DB_HOST=os.getenv("DB_HOST")
DB_PORT=int(os.getenv("DB_PORT"))
DB_USER=os.getenv("DB_USER")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_NAME=os.getenv("DB_NAME")
S3_ENDPOINT=os.getenv("S3_ENDPOINT")
S3_ACCESS_KEY=os.getenv("S3_ACCESS_KEY")
S3_SECRET_KEY=os.getenv("S3_SECRET_KEY")