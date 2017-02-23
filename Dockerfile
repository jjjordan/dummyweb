FROM python:3.6-slim
MAINTAINER John J. Jordan <jj@jjjordan.io>

CMD ["/bin/sh", "/start.sh"]
EXPOSE 5000
RUN pip install flask python-dateutil
ADD run.py start.sh /
