FROM python:3.10-slim

WORKDIR /app

COPY /requirements.txt ./requirements.txt
COPY /modular_code ./modular_code
COPY /model ./model
COPY /app.py ./app.py

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8506

ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"]




