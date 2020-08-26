FROM library/python:3.8.5-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY VERSION entrypoint.sh app.py ./
ENTRYPOINT ["/app/entrypoint.sh"]
