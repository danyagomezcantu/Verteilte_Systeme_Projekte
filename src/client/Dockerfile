FROM python:3.10.11
WORKDIR /app
COPY client.py /app/
COPY REST_API.py /app/
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
LABEL authors="Sven"
CMD ["python", "client.py"]
