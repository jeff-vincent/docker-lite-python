import docker
from docker_lite_python.docker_lite import DockerLite

dl = DockerLite()


def test_run_container():
	test_container_name = 'test-container'
	# first check that a conainer by the 
	# test name doesn't exist.
	if dl.get_container_by_name('test-container'):
		dl.kill_container('test-container')

	response = dl.run_container('alpine', 'test-container', 'echo "Hello World!"')

	assert response == b'Hello World!\n'

	dl.kill_container('test-container')
