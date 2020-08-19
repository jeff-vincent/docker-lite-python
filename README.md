[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)




# docker-lite-python
A simple, Python-based Docker interface built on top of the [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/). 
Intended to programmatically spin up, pass communications to, and ultimately tear down single Docker containers.
Requires a local instance of Docker.

**[Quick Start](#quick-start)** | **[Reference](#reference)** | **[Examples](#examples)**


## Quick Start:
```
$ sudo python3
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
||`*resulting_image_name*: string`|`Enforces best practice of explicitly naming images.`|
||||
|`list_containers()`|`*all*: bool: default=False`|`List running containers by default.`|
||||
|`run_container()`|`*image_name*: string`|`Run a Docker container, optionally with a command.`|
||`*resulting_container_name*: string`|`Enforces best practice of explicitly naming containers.`|
||`*command*: string: The command to run. `|`Optional.`|
||||
|`get_container_by_name()`|`*existing_container_name*: string`|`Get a Docker container by name.`|
||||
|`exec_into_running_container()`|`*existing_container_name*: string`|`Run a command in an active container.`|
||`*command*: string: The command to execute in the running Docker container.`|
||||
|`kill_container()`|`*existing_container_name*: string`|`Shut down and delete a container.`|
||||

## Examples:
```
from docker_lite import DockerLite

dl = DockerLite()
```
`dl.build_image('./Dockerfile', 'my-image')` # build a Docker image called 'my-image' from a Dockerfile

`dl.list_containers(all=True)` # list all containers. Default is to list running containers

run a Docker container called 'my-container' based on a Docker image called 'my-image'

`dl.run_container('my-image', 'my-container')` 

run a terminal command in a running Docker container called 'my-container'. Be creative

`dl.exec_into_running_container('my-container', 'echo "Hello World!"')`

`container = dl.get_container('my-container')` # get a container called 'my-container' by its unique name
 - [Python Docker SDK documentation on container objects here](https://docker-py.readthedocs.io/en/stable/containers.html#container-objects)

`dl.kill_container('my-container')` # kill a container called 'my-container' by its unique name
