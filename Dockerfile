FROM python:3-alpine

WORKDIR /opt/gn_juridico_igpm

RUN apk update 

RUN apk add py3-pip build-base

RUN pip install beautifulsoup4 pandas openpyxl
RUN mkdir shared

ADD IGP_DI.py .
ADD IGPM_MFGV.py .
ADD IPCA.py .
ADD Main.py .

CMD ["Main.py"]

ENTRYPOINT ["python3"]