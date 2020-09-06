print("Welcome to component generator v1.0.0")

component_name = input("Component name: ")
component_inherit = input("Component inherit: ")

component_template = f"""from PyQt5.QtWidgets import {component_inherit}

class {component_name}({component_inherit}):
	
	def __init__(self):
		super({component_name}, self).__init__()
		# Put code here
	
	def getDefaultProps(self): 
		# Props Inspector
		pass

	def getInitialState(self):
		pass

	def executeProps(self):
		pass

	def componentWillMount(self):
		pass

	def render(self):
		pass

	def componentDidMount(self):
		pass

	def destroy(self):
		pass

	def componentWillUnmount(self):
		pass

	def componnetDidUpdate(self):
		pass

"""



with open('./components/{}.py'.format(component_name).lower(), 'w') as file:
	file.write(component_template)
	file.close()


