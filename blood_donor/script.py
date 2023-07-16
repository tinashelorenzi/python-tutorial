import sqlite3

connection = sqlite3.connect('blood_donors.db')
cursor = connection.cursor()
continueflag = True

while(continueflag == True):
    name = input("Enter donor name: ")
    age = int(input("Enter an age: "))
    blood_type = input("Ender blood type: ")
    recepient = input("Enter recepient name: ")

    cursor.execute("INSERT INTO donors (name, age, blood_type, recepient) VALUES (?, ?, ?, ?)", (name, age, blood_type, recepient))
    connection.commit()
