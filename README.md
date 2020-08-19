# docker-lite-python
A simple, Python-based Docker interface. Requires a local instance of Docker.

## Quick Start:
```
>>>from docker_light import DockerLite
>>>dl = DockerLite()
```

start an Alpine image and keep it running
```
>>>dl.run_container('alpine:latest', 'alpine-container', 'sleep infinity')
```
exec into the running container
```
>>>dl.exec_into_running_container('alpine-container', 'echo "hello world"')
ExecResult(exit_code=0, output=b'hello world\n')
```
tear down that container!
```
>>>dl.kill_container('alpine-container')
200
```

## Reference:

| Available Methods | Args|Overview|
|--------|-----|----|
|`build_image()` | `*path_to_dockerfile*: string`|`Build a Docker image from a local Dockerfile.`|
|| `*resulting_image_name*: string`|
||||
|` list_containers()`|`all: bool`|`List running containers by default.`|



## Examples
```
from docker_lite import DockerLite

dl = DockerLite()
```
build an image from a Dockerfile

`dl.build_image('./Dockerfile', 'my-container')`

list all containers

`dl.list_containers(all=True)`






