# docker-lite-python
A simple, Python-based Docker interface. Requires a local instance of Docker.

## Quick Start:
```
$ python3
>>>from docker_light import DockerLite
>>>dl = DockerLite()
```

start an Alpine image and keep it running
```
>>>dl.run_container('alpine:latest', 'alpine-container', 'sleep infinity')
```
exec into the running container
```
>>>dl.exec_into_running_container('alpine-container', 'echo "Hello World!"')
ExecResult(exit_code=0, output=b'Hello World!\n')
```
tear down that container!
```
>>>dl.kill_container('alpine-container')
200
```

## Reference:

| Methods | Args | Overview |
|---------|------|----------|
|`build_image()`|`*path_to_dockerfile*: string`|`Build a Docker image from a local Dockerfile.`|
||`*resulting_image_name*: string`|
||||
|`list_containers()`|`*all*: bool: default=False`|`List running containers by default.`|
||||
|`run_container()`|`*image_name*: string`|`Run a Docker container, optionally with a command.`|
||`*resulting_container_name*: string`|
||`*command*: string: The command to run. `|`Optional.`|
||||
|`get_container_by_name()`|`*existing_container_name*: string`|`Get a Docker container by name.`|
||||
|`exec_into_running_container()`|`*existing_container_name*: string`|`Run a command in an active container.`|
||`*command*: string: The command to execute in the running Docker container.`|
||||
|`kill_container()`|`*existing_container_name*: string`|`Shut down and delete a container.`|
||||

## Examples
```
from docker_lite import DockerLite

dl = DockerLite()
```
`dl.build_image('./Dockerfile', 'my-image')` # build a Docker image called 'my-image' from a Dockerfile

`dl.list_containers(all=True)` # list all containers. Default is to list running containers

run a Docker container called 'my-container' based on a Docker image called 'my-image'

`dl.run_container('my-image', 'my-container')` 

`dl.get_container('my-container')` # get a container called 'my-container' by its unique name

run a terminal command in a running Docker container called 'my-container'. Be creative

`dl.exec_into_running_container('my-container', 'echo "Hello World!"')`

`dl.kill_container('my-container')` # kill a container called 'my-container' by its unique name
