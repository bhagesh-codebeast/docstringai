from modules import parse_functions, model_functions, clean_code

class generate_docstring:
	"""
	module to generate docstring for Python scripts.
	input:
		model_name
		script_path
		...
	output:
		...
	"""
	def __init__(self, model_name = '', script_path = '', output_path = ''):
		self.model = model_name
		self.script = script_path
		self.output = output_path
	def parse_code(self):
		print('...')
	def prompt_model(self):
		print('...')
	def clean_code(self):
		print('...')
	def save_code(self):
		print('...')

if __name__ == "__main__":
	instance = generate_docstring()
	import ollama
	print(ollama.list())