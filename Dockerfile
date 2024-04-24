FROM python:3.12.1

ENV PYTHONUNBUFFERED 1

WORKDIR /userauthsite

RUN pip install --upgrade pip

COPY requirements.txt /userauthsite/

RUN pip install -r requirements.txt

COPY . /userauthsite/

RUN pip install python-dotenv

EXPOSE 8000

CMD ["python", "userauthsite/manage.py", "runserver", "0.0.0.0:8000"]