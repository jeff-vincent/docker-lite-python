import docker
from docker_lite import DockerLite

dl = DockerLite()
CONTAINER_NAME = 'test-container'

def test_run():
        container = dl.run_container(
                image_name='alpine',
                resulting_container_name=CONTAINER_NAME)
        assert container.name == CONTAINER_NAME
        container.stop()

def test_exec():
        container = dl.run_container(
                image_name='alpine',
                command='sleep infinity',
                resulting_container_name=CONTAINER_NAME)
        response = dl.exec_into_running_container(container.name, 'echo "Hello World!"')
        assert "output=b'Hello World!\\n'" in str(response)
        container.stop()



