import ollama

class get_response:
	def __init__(self, model, prompt):
		self.model = model
		self.prompt = prompt
	def check_model(self):
		try:
			ollama.chat(self.model)
		except ollama.ResponseError as e:
			print('Error:', e.error)
			if e.status_code == 404:
				ollama.pull(self.model)
	def ask_model(self):
		self.check_model()
		response = ollama.generate(self.model, self.prompt)
		return response['response']

if __name__ == "__main__" :
	model = 'llama3'
	prompt = 'write a well formated docstring for the following python function: def add(num1,num2): return num1+num2'
	instance = get_response(model, prompt)
	print(instance.ask_model())

# python3 /data/modules/model_functions.py &>> response.txt &