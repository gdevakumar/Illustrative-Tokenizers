FROM python:3.12

WORKDIR /tokenizer

COPY . .

EXPOSE 5000

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]

