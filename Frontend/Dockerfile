FROM node:alpine

RUN apk update \
  && apk add --update alpine-sdk \
  && npm install -g @angular/cli@1.4.8 \
  && apk del alpine-sdk \
  && apk add --no-cache bash \
  && rm -rf /tmp/* /var/cache/apk/* *.tar.gz ~/.npm \
  && npm cache clear --force

ADD package.json /tmp/package.json
RUN cd /tmp && npm install
RUN mkdir -p /var/www/html/frontend/dist \
  && cp -a /tmp/node_modules /var/www/html/frontend


WORKDIR /var/www/html/frontend
VOLUME /var/www/html/frontend
COPY ./ ./
ADD init.sh /
RUN chmod +x /init.sh
ENTRYPOINT ["/init.sh"]
