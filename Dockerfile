FROM python:3.8-slim-buster
COPY .  /string_calculator
WORKDIR /string_calculator
RUN pip install -r requirements.txt
EXPOSE  5000
CMD ["python", "string_calculator/flask_main.py"]
