import os

"""
open(\C:\Users\Home\Documents\Material de Estudo\Python\Curso 30 Days of Python\Days10-20\templates\email_message.txt).read()
"""

def get_template_path(path):
	file_path = os.path.join(os.getcwd(), path)
	if not os.path.isfile(file_path):
		raise Exception("This is not a valid template path")
	return file_path

def	get_template(path):
	file_path = get_template(path)
	return open(file_path).read()
	

file_ = '\C:\Users\Home\Documents\Material de Estudo\Python\Curso 30 Days of Python\Days10-20\templates\email_message.txt'	

print(get_template(file_))