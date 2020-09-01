import random
from flask import Flask
from flask import session
from flask import request
from docker_lite_python import DockerLite

app = Flask(__name__)
dl = DockerLite()
app.secret_key = 'SECRET_KEY'

@app.route('/', methods=['GET'])
def index():
    return 'Service is up.'

@app.route('/run-container', methods=['GET'])
def run_container():
    container_name = random.random()
    session['container_name'] = str(container_name)
    env = 'alpine:latest'
    cmd = 'sleep infinity'
    container = dl.run_container(env, container_name, cmd)
    return 'Container {} running.'.format(container.name)

@app.route('/exec-into-running-container', methods=['POST'])
def exec_into_running_container():
    cmd = request.form.get('cmd')
    container_name = session['container_name']
    result = dl.exec_into_running_container(container_name, cmd)
    return str(result)

@app.route('/kill-container', methods=['GET'])
def kill_container():
        container_name = session['container_name']
        dl.kill_container(container_name)
        return 0

if __name__ == '__main__':
    app.run(debug=True)