from argparse import ArgumentParser
from docker_lite_python import DockerLite

class ExampleAdapter:

	def __init__(self):
		self.dl = DockerLite()
		self.dfile_path = './'

	def generate_container(self):
		image = self.dl.build_image(
					path_to_dir=self.dfile_path, 
					resulting_image_name='legacy-env')
		container = dl.run_container(
					image_name='legacy-env',
					resulting_container_name='legacy-env',
					command='sleep infinity')
		return container

	def pass_input(self, container_name, input):
		intermediate_result = dl.exec_into_running_container(
					existing_container_name=container_name,
					command=example_input)
		return intermediate_result.output

	def pass_output(self, intermediate_result):
		adapted_result = intermediate_result + ' and some more stuff in Python or beyond!'
		return adapted_result

	def tidy_up(self):
		dl.remove_all_images()
		dl.kill_container('legacy-env')


def main():
	ea = ExampleAdapter()
	parser = ArgumentParser()
	# g++ -o qq qq.cpp
    	parser.add_argument('example_input1', help='type: string: compile the "sub-code."')
   	# ./qq
    	parser.add_argument('example_input2', help='type: string: run the "sub-code."')
   	args = parser.parse_args()
	container = ea.generate_container()
	intermediate_result = ea.pass_input(container.name, args.example_input1)
	intermediate_result = ea.pass_input(container.name, args.example_input2)
	adapted_result = ea.pass_output(intermediate_result)
	ea.tidy_up()
	return adapted_result

if __name__ == '__main__':
	main()


