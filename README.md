# Python Starter Project

## Contact details

* Jonathan Zwart <jz@sprinthive.com>
* Monday 9 April 2018 


## Ports

* 9090: uwsgi (server)
* 9191: uwsgitop (server stats)


## References

* http://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html

##Key steps

### Repository check-out

1. `gcloud init`
2. `gcloud source repos clone python-starter-project --project=jons-world`
3. `cd python-starter-project`
4. `git checkout ground-zero`

### Docker build

The build size is currently 711 MB

5. `docker build -t python-starter-test .`
6. `docker run --name python-starter-test -e PYTHONUNBUFFERED=0 -p 9090:9090 -p 9191:9191 python-starter-test`

### Tests via curl

7. Base URL `curl 127.0.0.1:9090`
8. Hello World `curl 127.0.0.1:9090/HelloWorld`
9. Import tests `curl 127.0.0.1:9090/TestImports`

### UWSGI statistics and load testing

10. For server stats, `uwsgitop 127.0.0.1:9191`
11. For load-testing (note trailing slash), e.g. `ab -n 1000 -c 2 http://127.0.0.1:9090/`


### Tear down

12. `docker stop python-starter-test`
13. `docker rm python-starter-test`
14. `docker rmi python-starter-test`

### Troubleshooting

1. Shell access:
 
     `docker exec -t -i python-starter-test /bin/bash`

2. Testing uwsgi by starting it manually:

    `uwsgi --http-socket 0.0.0.0:9090 --wsgi-file app/main.py --master --processes 4 --threads 2 --stats 0.0.0.0:9191 --callable app`

3. UWSGI settings: `app/uwsgi.ini`

4. Add new python modules in: `app/requirements.txt`

*That's it!*