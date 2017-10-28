FROM python:alpine


COPY requirements.txt /

RUN set -e; \
	apk add --no-cache --virtual .build-deps \
		gcc \
		libc-dev \
		linux-headers \
  && pip install virtualenv \
  && pip install -r requirements.txt \
	&& apk del .build-deps \
  && rm -rf /tmp/* /var/cache/apk/* *.tar.gz

RUN mkdir -p /var/www/backend
WORKDIR /var/www/backend

COPY ./ ./
EXPOSE 9090
CMD [ "uwsgi", "--socket", "0.0.0.0:9090", "--plugins", "python3", "--protocol", "uwsgi", "--module", "wsgi:app"]
