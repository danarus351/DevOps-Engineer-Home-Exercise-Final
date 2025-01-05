FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
expose 5000
ENTRYPOINT ["python", "rick_morty_api.py"]