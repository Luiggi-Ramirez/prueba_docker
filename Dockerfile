FROM python:3.10.4 
ENV PYTHONUNBUFFERED=1 
RUN mkdir /user_test 
WORKDIR /user_test  
COPY . /user_test/
COPY req.txt /user_test/
RUN pip install -r req.txt
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]