FROM python
RUN pip install django==3.2
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver"]