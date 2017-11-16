FROM python:2.7.14-stretch

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt ./requirements.txt
RUN pip install -r /app/requirements.txt

COPY ./ ./

# RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main" > /etc/apt/sources.list.d/pgdg.list \
#     && apt-get install wget ca-certificates \
#     && wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
#     && apt-get -y update && apt-get -y upgrade \
#    && apt-get install -y postgresql-9.6

CMD ["python", "app.py"]
