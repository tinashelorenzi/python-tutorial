import sqlite3

# Function to create the contact table if it doesn't exist
def create_table():
    connection.execute('''CREATE TABLE IF NOT EXISTS contacts (
                         id INTEGER PRIMARY KEY,
                         name TEXT,
                         email TEXT,
                         phone TEXT,
                         notes TEXT
                      )''')
    connection.commit()

# Function to add a new contact
def add_contact():
    name = input("Enter full name: ")
    email = input("Enter email address: ")
    phone = input("Enter phone number: ")
    notes = input("Enter any notes (optional): ")

    connection.execute("INSERT INTO contacts (name, email, phone, notes) VALUES (?, ?, ?, ?)", (name, email, phone, notes))
    connection.commit()
    print("Contact added successfully!\n")

# Function to view all contacts
def view_contacts():
    cursor = connection.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("No contacts found.\n")
    else:
        print("All Contacts:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Phone: {row[3]}, Notes: {row[4]}")
        print()

# Function to search for a contact by name
def search_contact():
    name = input("Enter the name to search for: ")
    cursor = connection.execute("SELECT * FROM contacts WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("Contact not found.\n")
    else:
        print("Search Results:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Phone: {row[3]}, Notes: {row[4]}")
        print()

# Main program
if __name__ == "__main__":
    # Connect to the database (creates one if it doesn't exist)
    connection = sqlite3.connect("contacts.db")
    create_table()

    while True:
        print("Options:")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Search for a contact by name")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.\n")

    # Close the database connection
    connection.close()