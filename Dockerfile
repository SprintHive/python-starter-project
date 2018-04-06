FROM tiangolo/uwsgi-nginx-flask:python2.7
#-alpine3.7

COPY ./app /app
COPY ./resources/nginx/nginx.conf /etc/nginx/conf.d/
COPY ./app/uwsgi.ini /etc/uwsgi/uwsgi.ini

WORKDIR /app
RUN pip install -U setuptools pip
RUN pip install -r /app/requirements.txt

ENV UWSGI_INI /etc/uwsgi/uwsgi.ini
#ENV LISTEN_PORT 3031

EXPOSE 5002 3031 9191 80 90

#CMD ["python", "test_app.py"]
#CMD ["./launch_server.sh"]