import os
import csv

os.getcwd()
os.chdir('C:\\Users\\Home\\Documents\\Material de Estudo\\Python\\Curso 30 Days of Python\\CSV_Examples')

# Creating a csv file
with open("data.csv", "w+") as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(["Title", "Description"])
	writer.writerow(["Row 1", "Some desc"])

# Override a csv file
with open("data.csv", "w+") as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(["Title", "Description", "Col 3"])
	writer.writerow(["Row 1", "Some desc", "Another"])	
	writer.writerow(["Row 1", "Some desc", "Another"])	
	writer.writerow(["Row 1", "Some desc", "Another"])	

# Append to a file
with open("data.csv", "a") as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(["Append row", "Some desc", "Another"])
	
	