FROM tiangolo/uwsgi-nginx-flask:python2.7

COPY ./app /app

# Copy config files
COPY config /etc/nginx/conf.d/
COPY ./app/uwsgi.ini /etc/uwsgi/uwsgi.ini

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
EXPOSE 9090 9191

# Place any commands here
#CMD ["python", "test_app.py"]
#CMD ["./launch_server.sh"]