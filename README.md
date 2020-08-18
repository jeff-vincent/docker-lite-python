# docker-lite-python
A simple, Python-based Docker interface. Requires a local instance of Docker.

## Usage:
```
>>>from docker_light import DockerLite
>>>dl = DockerLite()

# start an Alpine image and keep it running

>>>dl.run_container('alpine:latest', 'alpine-container', 'sleep infinity')

# exec into the running container

>>>dl.exec_into_running_container('alpine-container', 'echo "hello world"')
ExecResult(exit_code=0, output=b'hello world\n')
```


