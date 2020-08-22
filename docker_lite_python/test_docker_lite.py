import docker
from docker_lite import DockerLite

dl = DockerLite()


def test_run():
        test_container_name = 'test-container'
        response = dl.run_container('alpine', test_container_name, 'echo "Hello World!"')
        assert response == b'Hello World!\n'
        
def test_get():
        container = dl.get_container_by_name('test-container')
        assert container.name == 'test-container'

def test_exec():
        test_container_name = 'exec-container'
        dl.run_container('alpine', test_container_name, 'sleep infinity')
        response = dl.exec_into_running_container(test_container_name, 'echo "Hello World!"')
        assert response == "ExecResult(exit_code=0, output=b'Hello World!\n')"
        



