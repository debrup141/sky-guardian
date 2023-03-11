FROM python:3.9
RUN pip install django==3.2
RUN mkdir /Sky-Guardian
WORKDIR /Sky-Guardian
ADD . /Sky-Guardian/
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python","manage.py","runserver","0.0.0.0:8000"]

