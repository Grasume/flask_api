FROM python:3.10.13

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
 
# Set up Flask application in development mode
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

COPY . .
COPY .. .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT [ "python3" ]
CMD [ "./main.py"]

