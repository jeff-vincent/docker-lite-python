import docker


class DockerLite:

    def __init__(self):
        self.client = docker.from_env()


    def build_image(self, path_to_dockerfile, resulting_image_name):
        response = self.client.images.build(
                    path=path_to_dockerfile, tag=resulting_image_name)
        return response


    def run_container(self, image_name, resulting_container_name, command=None):
        response = self.client.containers.run(
                    image=image_name,  
                    name=resulting_container_name, 
                    command=command,
                    remove=True)
        return response


    def exec_into_running_container(self, existing_container_name, command):
        container = self.client.containers.get(existing_container_name)
        response = container.exec_run(command)
        return response


    def kill_container(self, existing_container_name):
        container = self.client.containers.get(existing_container_name)
	container.stop()
	container.remove()
        return 200


    def list_containers(self, all=None):
        if all:
            response = self.client.containers.list(all=True)
        else:
            response = self.client.containers.list()
        return response
