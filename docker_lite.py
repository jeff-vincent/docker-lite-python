import docker


class DockerLite:

    def __init__(self):
        self.client = docker.from_env()


    def build_image(self, path_to_dockerfile, resulting_image_name):
        """A method to build a Docker image from a Dockerfile. 
        Args:
            path_to_dockerfile: string: the path to the Dockerfile
            resulting_image_name: string: unique name for the image
        Returns:
            response: 
        """
        response = self.client.images.build(
                    path=path_to_dockerfile, tag=resulting_image_name)
        return response


    def list_containers(self, all=None):
        """A method for listing Docker containers. 
        Returns only running Docker containers by default.
        Args:
            all: bool: optional
        Returns:
            response: 
        """
        if all:
            response = self.client.containers.list(all=True)
        else:
            response = self.client.containers.list()
        return response


    def get_container_by_name(self, existing_container_name):
        """A method for getting a Python object that represents
        a given Docker container.
        Args:
            existing_container_name: string: the name of the Docker container
        Returns:
            response: Python object: a given Docker container
        """
        response = self.client.containers.get(existing_container_name)
        return response


    def run_container(self, image_name, resulting_container_name, command=None):
        """A method for running a Docker container. 
        Requires a name for the container.
        Args:
            image_name: string: the name of the Docker image to run
                        can be local or in Docker Hub.
            resulting_container_name: string: the name to set to the container
            command: string: the command to run at Docker container startup: optional
        Returns:
            response: 
        """
        response = self.client.containers.run(
                    image=image_name,  
                    name=resulting_container_name, 
                    command=command,
                    remove=True)
        return response


    def exec_into_running_container(self, existing_container_name, command):
        """A method for executing a command in a running Docker container.
        Args:
            existing_container_name: string: the container in which to execute the command
            command: string: the command to run in the Docker container
        Returns:
            response: 
        """
        container = self.get_container_by_name(existing_container_name)
        response = container.exec_run(command)
        return response


    def kill_container(self, existing_container_name):
        """A methond for stopping and removing a Docker container.
        Args: 
            existing_container_name: string: the container to kill
        Returns:
            200
        Than"""
        container = self.get_container_by_name(existing_container_name)
        container.stop()
        container.remove()
        return 200
