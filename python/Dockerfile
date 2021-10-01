FROM python:3
WORKDIR /usr/src/app
RUN pip install --no-cache-dir psycopg2
COPY . .
CMD [ "python", "./script.py" ]
EXPOSE 8080
