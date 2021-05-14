FROM csighub.tencentyun.com/medipedia/medi-py:1.0

WORKDIR /usr/local/services/ams_feedback

ADD requirements.txt /usr/local/services/ams_feedback/
RUN yum -y upgrade && \
    yum install -y libcurl-devel && \
    pip3 install --upgrade pip && \
    export PYCURL_SSL_LIBRARY=nss && \
    pip3 install -r /usr/local/services/ams_feedback/requirements.txt

COPY ./ /usr/local/services/ams_feedback/

#RUN python3 manager.py db init
#RUN python3 manager.py db migrate
#RUN python3 manager.py db upgrade

COPY notice.ini /etc/supervisord.d/
COPY start.sh /etc/kickStart.d/