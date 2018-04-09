FROM tiangolo/uwsgi-nginx-flask:python2.7
#FROM tiangolo/uwsgi-nginx-flask:python2.7-alpine3.7

COPY ./app /app

# Copy config files
COPY ./resources/nginx/nginx.conf /etc/nginx/conf.d/
COPY ./app/uwsgi.ini /etc/uwsgi/uwsgi.ini

# Install requirements
# Note that changing requirements.txt will trigger a rebuild every time
# To avoid this, add pip install commands here line by line

WORKDIR /app
RUN pip install -U setuptools pip
RUN pip install -r /app/requirements.txt

# UWSGI environment [not clear these are used]
ENV UWSGI_INI /etc/uwsgi/uwsgi.ini
#ENV LISTEN_PORT 3031

# Expose ports
EXPOSE 5002 3031 9191 80 90

# Place any commands here
#CMD ["python", "test_app.py"]
#CMD ["./launch_server.sh"]