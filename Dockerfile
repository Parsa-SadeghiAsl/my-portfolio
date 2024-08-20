FROM python:3.12.0-slim-bullseye

WORKDIR /app

COPY . /app


RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python3", "./portfolio/manage.py", "runserver", "0.0.0.0:8000"]
