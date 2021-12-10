FROM alpine

RUN apk add --update python3 py3-pip
RUN apk --no-cache add curl && pip install hvac && apk add --no-cache bash
    
RUN mkdir /home/app
WORKDIR /home/app

COPY app/ /home/app/


EXPOSE 8200

CMD python3 app.py



