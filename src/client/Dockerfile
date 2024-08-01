FROM python:3.10.11
WORKDIR /app
#imports files to folder /app/
COPY client.py /app/
COPY REST_API.py /app/
COPY requirements.txt /app/
#could not install dependencies
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
LABEL authors="Sven"
CMD ["python", "client.py"]
#if you are in the dockerfile directory you can build this image with the command:
# "docker build -t vs_client ."