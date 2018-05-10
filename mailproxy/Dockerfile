FROM python:3.6.5-slim
MAINTAINER Viettel Cloud Project <cloud@viettel.com.vn> 
LABEL Vendor="Viettel Network" \
      License=MIT \
      Version=1.0.0

ENV http_proxy "http://10.61.2.237:3128"
ENV https_proxy "http://10.61.2.237:3128"

COPY mailproxy.py /

RUN pip install -U aiosmtpd

EXPOSE 9011

CMD [ "python3", "./mailproxy.py", "/etc/mailproxy/config.ini" ]
