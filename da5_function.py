items = ["Mic", "Phone", 323,12, 3123,123, "Justin", "Bag", "Cliff Bars", 134]

str_items = []
num_items = []

for i in items:
	if isinstance(i, float) or isinstance(i, int):
		num_items.append(i)
	elif isinstance(i, str):
		str_items.append(i)
	else:
		pass

		
print(str_items)
print(num_items)		


items = ["Mic", "Phone", 323,12, 3123,123, "Justin", "Bag", "Cliff Bars", 134]

#Função que vare a lista, e adiciona os itens em novas listas de acordo com o seu tipo
def parse_lists(some_list):
	str_list_items = []
	num_list_items = []
	for i in some_list:
		if isinstance(i, float) or isinstance(i, int):
			num_list_items.append(i)
		elif isinstance(i, str):
			str_list_items.append(i)
		else:
			pass
	return 	str_list_items, num_list_items
	
	
print(parse_lists(items))

items2 = ["Mic", "Phone", [123, 321, "adf"]]

print(parse_lists(items2))


sum([123, 323, 423])

def my_sum(my_num_list):
	total = 0
	for i in my_num_list:
		if isinstance(i, float) or isinstance(i, int)
			total += i
	return total
	
	