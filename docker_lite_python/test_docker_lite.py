import docker
from docker_lite import DockerLite

dl = DockerLite()


def test_run():
        test_container_name = 'test-container'
        # first check that a conainer by the 
        # test name doesn't exist.
        # try:
            # if dl.get_container_by_name('test-container'):
                # dl.kill_container('test-container')
        # except:
            # pass
        response = dl.run_container('alpine', 'test-container', 'echo "Hello World!"')

        assert response == b'Hello World!\n'

        # dl.kill_container('test-container')

