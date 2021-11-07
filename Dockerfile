FROM python:3.7-alpine
COPY .  /string_calculator
WORKDIR /string_calculator
RUN pip install -r requirements.txt
RUN pip install --ignore-installed six watson-developer-cloud
EXPOSE  5000
CMD ["python", "string_calculator/flask_main.py"]
