FROM node:alpine

RUN apk update \
  && apk add --update alpine-sdk \
  && npm install -g @angular/cli@1.4.8 \
  && apk del alpine-sdk \
  && apk add --no-cache bash \
  && rm -rf /tmp/* /var/cache/apk/* *.tar.gz ~/.npm \
  && npm cache clear --force \
  && mkdir -p /var/www/frontend/dist

VOLUME /var/www/frontend
WORKDIR /var/www/frontend

COPY ./ ./
#RUN  npm install

ENTRYPOINT ["ng", "build"]
