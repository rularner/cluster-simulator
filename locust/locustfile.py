from locust import HttpLocust, TaskSet, task, web
from flask import render_template, request

class WebsiteTasks(TaskSet):
    def on_start(self):
        self.client.post("/login", {
            "username": "test_user",
            "password": ""
        })
    
    @task
    def index(self):
        self.client.get("/")
        
    @task
    def about(self):
        self.client.get("/about/")

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000

@web.app.route("/normal_load", methods=['GET', 'POST'])
def normal_load():
    if request.method == 'DELETE':
        WebsiteUser.min_wait = Websuteuser.max_wait = 1000000000000
        return "OK"
    elif request.method == "GET":
        #WebsiteUser.min_wait = 5000
        #WebsiteUser.max_wait = 15000
        return "OK"

@web.app.route("/control")
def main():
    return """
<html lang="en">
 
<head>
    <title>Controller App</title>
 
 
    <link href="http://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">
 
    <link href="http://getbootstrap.com/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">
 
 
</head>
 
<body>
 
    <div class="container">
        <div class="header">
            <nav>
                <ul class="nav nav-pills pull-right">
                    <li role="presentation" class="active"><a href="#">Home</a>
                    </li>
                </ul>
            </nav>
            <h3 class="text-muted">Python Flask App</h3>
        </div>
 
        <div class="jumbotron">
            <h2>Controller App</h2>
            <p class="lead"></p>
            <ul>
              <li><a href="http://:5000">main app</a></li>
              <li><a href="http://:9090">Prometheus (monitoring)</a></li>
              <li><a href="http://:9090/graph?g0.range_input=1h&g0.expr=flask_request_count&g0.tab=0">Prometheus request graph</a></li>
              <li><a href="http://:8089">Locust (load generator)</a></li>
            </ul>
            </p>
        </div>
        <div class="jumbotron">
          <h2>Scenarios</h2>
          <ul>
            <li><a href="/normal_load-stop">Stop normal load</a></li>
            <li><a href="/normal-load-stop">Start normal load</a></li>
          </ul>
        </div>
 

        <footer class="footer">
            <p>&copy; Rusty Larner 2017</p>
        </footer>
 
    </div>
</body>
 
</html>
"""
