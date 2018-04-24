# Python Starter Project

## Contact details

* Jonathan Zwart / Dane Bezuidenhout
* Tuesday 24 April 2018 

## Ports

* 8080: uwsgi (server)
* 8181: uwsgitop (server stats)

## References

* http://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html

##Key steps

### Repository check-out

1. `git clone git@github.com:SprintHive/python-starter-project.git`
2. `cd python-starter-project`
3. `git checkout ground-zero`

### Docker build

This image size is approx. 700MB

4. `docker build -t python-starter-project .`
5. `docker run --name python-starter-project -e PYTHONUNBUFFERED=0 -p 8080:8080 -p 8181:8181 python-starter-project`

### Docker build (alpine - EXPERIMENTAL)

This image size is approx. 150MB

6. `docker build -f Dockerfile_alpine -t python-starter-project-alpine .`
7. `docker run --name python-starter-project-alpine -e PYTHONUNBUFFERED=0 -p 8080:8080 -p 8181:8181 python-starter-project-alpine`

### Tests via curl

8. Ping `curl 127.0.0.1:8080/ping`
9. Import tests `curl 127.0.0.1:8080/test-imports`
10. Logging tests `curl 127.0.0.1:8080/test-logging`

### UWSGI statistics and load testing

10. For server stats, `uwsgitop 127.0.0.1:8181`
11. For load-testing (note trailing slash), e.g. `ab -n 1000 -c 2 http://127.0.0.1:8080/`

### Tear down

12. `docker stop python-starter-project`
13. `docker rm python-starter-project`
14. `docker rmi python-starter-project`

### Minikube deployment

1. minikube start
2. eval $(minikube docker-env)
3. Run the Docker build command above
4. kubectl create -f config/kubernetes/deployment.yaml
5. kubectl get po -w
6. kubectl port-forward <pod name> 8080:8080
7. Browse to http://localhost:8080/ping
8. eval $(minikube docker-env -u)

### Troubleshooting

1. Shell access:
 
     `docker exec -t -i python-starter-project /bin/bash`

2. Testing uwsgi by starting it manually:

    `uwsgi --http-socket 0.0.0.0:8080 --wsgi-file app/main.py --master --processes 4 --threads 2 --stats 0.0.0.0:8181 --callable app`

3. UWSGI settings: `app/uwsgi.ini`

4. Add new python modules in: `app/requirements.txt`

*That's it!*