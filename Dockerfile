FROM python:3.12.5
WORKDIR /app
COPY . .
CMD ["python", "test.py"]