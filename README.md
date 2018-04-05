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