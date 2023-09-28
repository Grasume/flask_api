FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
 
# Set up Flask application in development mode
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

COPY . .

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r ./requirements.txt

#CMD touch test.json
ENTRYPOINT [ "python3" ]
CMD [ "./python/main.py"]

