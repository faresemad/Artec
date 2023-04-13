FROM Python
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver"]