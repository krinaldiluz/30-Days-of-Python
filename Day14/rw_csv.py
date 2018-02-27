import os
import csv

os.getcwd()
os.chdir('C:\\Users\\Home\\Documents\\Material de Estudo\\Python\\Curso 30 Days of Python\\Day14')
os.getcwd()

with open("data.csv", "w+") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Col 1", "Col 2"])
    writer.writerow(["Data 1", "Data 2"])



with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)



with open("data.csv", "a") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Data 3", "Data 4"])



with open("data.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)


with open("data.csv", "a") as csvfile:
    fieldnames = ["id", "title"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({"id": 123, "title": "New title"})