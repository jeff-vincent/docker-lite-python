import docker


class DockerPy:

    def __init__(self):
            self.client = docker.from_env()


    def start_container(self, image, container_name, command):
            response = self.client.containers.run(
                    image=image,  
                    name=container_name, 
                    command=command,
                    remove=True)
            return response


    def pass_command(self, container_name, command):
            container = self.client.containers.get(container_name)
            response = container.exec_run(command)
            return response


    def kill_container(self, container_name):
            container = self.client.containers.get(container_name)
 			container.stop()
			container.remove()
            return 200
