FROM tiangolo/uwsgi-nginx-flask:python2.7

ENV LISTEN_PORT 8080

COPY ./app /app

# Copy config files
COPY ./app/uwsgi.ini /etc/uwsgi/uwsgi.ini
# COPY config /etc/nginx/conf.d/

# Install requirements
# Note that changing requirements.txt will trigger a rebuild every time
# To avoid this, add pip install commands here line by line

WORKDIR /app
RUN pip install -U setuptools pip
RUN pip install -r /app/requirements.txt

# UWSGI environment [not clear these are used]
ENV UWSGI_INI /etc/uwsgi/uwsgi.ini

# Python logging
ENV LOG_CFG ./logging.yml

# Expose ports
EXPOSE 8080 8181

# Place any commands here
#CMD ["python", "test_app.py"]
#CMD ["./launch_server.sh"]
