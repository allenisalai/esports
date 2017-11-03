FROM node:alpine

RUN apk update \
  && apk add --update alpine-sdk \
  && npm install -g @angular/cli@1.4.8 \
  && apk del alpine-sdk \
  && apk add --no-cache bash \
  && rm -rf /tmp/* /var/cache/apk/* *.tar.gz ~/.npm \
  && npm cache clear --force \
  && mkdir -p /var/www/frontend/dist

WORKDIR /var/www/frontend

ADD package.json /tmp/package.json
RUN cd /tmp && npm install
COPY ./ ./
RUN cp -R /tmp/node_modules /var/www/frontend/node_modules

WORKDIR /var/www/frontend
VOLUME /var/www/frontend

ENTRYPOINT ["ng", "build"]
