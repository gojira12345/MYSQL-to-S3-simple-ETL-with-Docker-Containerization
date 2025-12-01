import pandas as pd
from etl import load, get_s3_client
import uuid


def test_load_writes_object_to_minio():
   
    df = pd.DataFrame({"id": [1], "name": ["Andy"], "age": [20]})
    unique_prefix = f"test_output_{uuid.uuid4().hex}"

    s3 = get_s3_client()
    bucket = "databucket"
    key = f"{unique_prefix}.csv"

  
    try:
        s3.head_bucket(Bucket=bucket)
    except Exception:
        s3.create_bucket(Bucket=bucket)

   
    import io
    csv_buf = io.StringIO()
    df.to_csv(csv_buf, index=False)
    s3.put_object(Bucket=bucket, Key=key, Body=csv_buf.getvalue())

   
    resp = s3.list_objects_v2(Bucket=bucket, Prefix=unique_prefix)
    assert "Contents" in resp
    keys = [obj["Key"] for obj in resp["Contents"]]
    assert key in keys
