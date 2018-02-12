from Classes_Example2 import make_messages

from py_day_mod.make_messages import MessageUser

obj = MessageUser()
obj.add_user("Justin", 123.32, email = 'hello@teamcfe.com')
obj.add_user("j0hn", 94.23)
obj.add_user("Sean", 93.23)
obj.add_user("Emilee", 193.23)
obj.add_user("Marie", 13.23)

print(obj.make_messages())

default_names = ["Justin", "john", "Emilee", "Jim", "Ron", "Sandra", "veronica", "Whitney"]
default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]

#make_messages(default_names, default_amounts)