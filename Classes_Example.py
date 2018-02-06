class Animal():
	name = 'Amy'
	noise = "Grunt"
	size = "Large"
	color = "brown"
	hair = "covers body"
	def get_color(self):
		return self.color
	@property	
	def make_noise(self):	
		return self.noise

dog = Animal()
dog.make_noise()
dog.size = "small"
dog.color = "black"
dog.hair = "hairless"

class Dog(Animal):
	name = 'Jon'
	# color = "brown"
	# def get_color(self):
	# 	return self.color

jon = Dog()
jon.color = 'white'
jon. name = "Jon Snow"


dog = Animal()
dog.get_color()

dog.make_noise


email_address = "another@gmail.com"
to_list = ['abc@gmail.com']
from_list = ['another2@gmail.com', 'hello@teamcfe.com']

def send_email(email=email_address, to_list=to_list, from_list=from_list):
	pass


