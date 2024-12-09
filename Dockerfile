FROM python:3.12-slim

WORKDIR web_form_validator/

COPY requirements.txt /web_form_validator/

RUN pip install -r requirements.txt

COPY . /web_form_validator/

RUN ["chmod", "+x", "./docker-entrypoint.sh"]
ENTRYPOINT ["bash", "-c"]
CMD ["./docker-entrypoint.sh"]