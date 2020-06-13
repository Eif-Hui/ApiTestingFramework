FROM python:3.7.3
WORKDIR .
ADD . .
RUN pip install -r requirements.txt
CMD ["pytest", "-q","manage.py","--alluredir","allure-results"]