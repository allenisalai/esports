FROM python:latest

COPY requirements.txt /

RUN mkdir -p /var/www/backend
WORKDIR /var/www/backend
VOLUME /var/www/backend

RUN pip install virtualenv virtualenvwrapper \
  	&& /bin/bash -c ". /usr/local/bin/virtualenvwrapper.sh ; mkvirtualenv esports" \
			&& pip install -r /requirements.txt

COPY ./ ./
EXPOSE 9090
CMD [ "uwsgi", "--socket", "0.0.0.0:9090", "--plugins", "python3", "--protocol", "uwsgi", "--module", "wsgi:app", "--py-autoreload", "1"]
