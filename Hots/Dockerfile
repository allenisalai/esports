FROM python:2.7.14-alpine3.4

COPY ./ /

RUN mkdir /hots_output

VOLUME /hots_output

RUN chmod +x /file_parse.sh

ENTRYPOINT ["/file_parse.sh"]
