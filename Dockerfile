#base image 
FROM python:3.11-slim

#working directory
WORKDIR /app/src

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /app/src

CMD ["tail","-f","/dev/null"]