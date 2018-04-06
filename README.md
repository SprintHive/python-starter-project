# Python Starter Project

* Jonathan Zwart <jz@sprinthive.com>
* Thurs 5 April 2018

Start at http://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html

1. `pip install uwsgi`

2. `pip install uwsgitop`

3. `uwsgi --http-socket 127.0.0.1:3031 --wsgi-file app/myflaskapp.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191 --callable app`

4. `uwsgitop 127.0.0.1:9191`

5. Single test: `curl 127.0.0.1:3031` -> `<span style='color:red'>I am app 1</span>`

7. Load test: `ab -n 1000 -c 2 http://127.0.0.1:3031/`

That's it!

## Ports

* 5002: keepalive service (or container shuts down)
* 3031: uwsgi
* 9191: uwsgitop

## Dockerization

1. `cd python-starter-project`

2. `docker build -t helloworld .`

3. `docker run --name helloworld -e PYTHONUNBUFFERED=0 -p 5002:5002 -p 3031:3031 -p 9191:9191 helloworld`

4. List ports: `docker port helloworld`

5. From outside: `curl 127.0.0.1:5002/hello`

6. From outside: `curl 127.0.0.1:5002/TestImports`

7. If you need SSH access, do: `docker exec -t -i helloworld /bin/bash`

8. Now repeat (3)-(5) above from within the container:

a. `uwsgi --http-socket 127.0.0.1:3031 --wsgi-file app/myflaskapp.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191 --callable app`

b. `uwsgitop 127.0.0.1:9191`

c. Single test: `curl 127.0.0.1:3031` -> `<span style='color:red'>I am app 1</span>`


9. Now launch uwsgi from within the container manually:

`uwsgi --http-socket 0.0.0.0:3031 --wsgi-file app/myflaskapp.py --master --processes 4 -\
-threads 2 --stats 0.0.0.0:9191 --callable app`

10. From outside, run: `uwsgitop 127.0.0.1:9191`

11. From outside, run: `curl 127.0.0.1:3031`

12. Load test: `ab -n 1000 -c 2 http://127.0.0.1:3031/`

13. Now modify Dockerfile to launch CMD: `launch_server.sh`

14. Repeat (10) and (11)

Hey presto!