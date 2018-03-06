import os
import csv
import shutil
from tempfile import NamedTemporaryFile

os.getcwd()
os.chdir('C:\\Users\\Home\\Documents\\Material de Estudo\\Python\\Curso 30 Days of Python\\CSV_Examples')
os.getcwd()

def get_length(file_path):
    with open("data.csv") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        print(reader_list)
        return len(reader_list)

def append_data(file_path, name, email):
    fieldnames = ['id', 'name', 'email']
    #the number of rows?
    next_id = get_length(file_path)
    with open(file_path, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({
                "id": next_id,
                "name": name,
                "email": email,
            })



#append_data("data.csv", "Justin", "hello@teamcfe.com")


filename = "data.csv"
temp_file = NamedTemporaryFile(delete=False)

with open(filename, "rb") as csvfile, temp_file:
    reader = csv.DictReader(csvfile)
    filename = ['id','name', 'email', 'amount', 'sent']
    writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
    writer.writerheader()

    for row in reader:
        print(row)
        writer.writerow({
                "id": row["id"],
                "name": row["name"],
                "email": row["email"],
                "amount": "1293.23",
                "sent": ""
            })

#shutil.move(temp_file, filename)
