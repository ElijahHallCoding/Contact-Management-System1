import os
import re

# Initialize an empty dictionary to store contacts
contacts = {}

def display_menu():
    print("\nWelcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file (*Bonus*)")
    print("8. Quit")

def add_contact():
    try:
        name = input("Enter the name: ").strip()
        phone = input("Enter the phone number: ").strip()
        email = input("Enter the email address: ").strip()

        # Validate phone number format (basic validation for digits only)
        if not re.fullmatch(r'\d{10}', phone):
            raise ValueError("Phone number must be 10 digits.")

        # Validate email format
        if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format.")

        # Check if contact already exists
        if phone in contacts:
            raise KeyError("A contact with this phone number already exists.")

        # Add contact to the dictionary
        contacts[phone] = {
            "name": name,
            "email": email
        }
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except KeyError as ke:
        print(f"Duplicate Error: {ke}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("Contact added successfully!")
    finally:
        print("Add contact operation completed.")

def edit_contact():
    try:
        phone = input("Enter the phone number of the contact you want to edit: ").strip()

        # Check if contact exists
        if phone not in contacts:
            raise KeyError("Contact not found.")

        name = input(f"Enter the new name ({contacts[phone]['name']}): ").strip()
        email = input(f"Enter the new email ({contacts[phone]['email']}): ").strip()

        # Use existing data if new input is empty
        name = name if name else contacts[phone]['name']
        email = email if email else contacts[phone]['email']

        # Validate email format
        if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format.")

        # Update contact information
        contacts[phone] = {
            "name": name,
            "email": email
        }
    except KeyError as ke:
        print(f"Lookup Error: {ke}")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("Contact updated successfully!")
    finally:
        print("Edit contact operation completed.")

def delete_contact():
    try:
        phone = input("Enter the phone number of the contact you want to delete: ").strip()

        # Attempt to delete the contact
        if phone in contacts:
            del contacts[phone]
        else:
            raise KeyError("Contact not found.")
    except KeyError as ke:
        print(f"Deletion Error: {ke}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("Contact deleted successfully!")
    finally:
        print("Delete contact operation completed.")

def search_contact():
    try:
        phone = input("Enter the phone number of the contact you want to search for: ").strip()

        # Retrieve and display contact information
        if phone in contacts:
            print(f"\nContact Details for {phone}:")
            print(f"Name: {contacts[phone]['name']}")
            print(f"Email: {contacts[phone]['email']}")
        else:
            raise KeyError("Contact not found.")
    except KeyError as ke:
        print(f"Search Error: {ke}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Search contact operation completed.")

def display_all_contacts():
    try:
        if not contacts:
            raise ValueError("No contacts available to display.")

        print("\nAll Contacts:")
        for phone, info in contacts.items():
            print(f"\nPhone: {phone}")
            print(f"Name: {info['name']}")
            print(f"Email: {info['email']}")
    except ValueError as ve:
        print(f"Display Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Display all contacts operation completed.")

def export_contacts():
    try:
        with open("contacts.txt", "w") as file:
            for phone, info in contacts.items():
                line = f"{phone},{info['name']},{info['email']}\n"
                file.write(line)
    except IOError as ioe:
        print(f"File Error: Unable to write to file. {ioe}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("Contacts successfully exported to 'contacts.txt'.")
    finally:
        print("Export contacts operation completed.")

def import_contacts():
    try:
        if not os.path.exists("contacts.txt"):
            raise FileNotFoundError("The file 'contacts.txt' does not exist.")

        with open("contacts.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:  # Skip empty lines
                    parts = line.split(",")
                    if len(parts) != 3:
                        raise ValueError(f"Incorrect format in line: {line}")
                    phone, name, email = parts

                    # Validate phone and email formats
                    if not re.fullmatch(r'\d{10}', phone):
                        raise ValueError(f"Invalid phone number format in line: {line}")
                    if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
                        raise ValueError(f"Invalid email format in line: {line}")

                    contacts[phone] = {"name": name, "email": email}
    except FileNotFoundError as fnfe:
        print(f"Import Error: {fnfe}")
    except ValueError as ve:
        print(f"Data Error: {ve}")
    except IOError as ioe:
        print(f"File Error: Unable to read file. {ioe}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("Contacts successfully imported from 'contacts.txt'.")
    finally:
        print("Import contacts operation completed.")

def main():
    while True:
        display_menu()
        choice = input("Select an option (1-8): ").strip()

        try:
            if choice == "1":
                add_contact()
            elif choice == "2":
                edit_contact()
            elif choice == "3":
                delete_contact()
            elif choice == "4":
                search_contact()
            elif choice == "5":
                display_all_contacts()
            elif choice == "6":
                export_contacts()
            elif choice == "7":
                import_contacts()  # Bonus task
            elif choice == "8":
                print("Thank you for using the Contact Management System. Goodbye!")
                break
            else:
                raise ValueError("Invalid menu option selected.")
        except ValueError as ve:
            print(f"Selection Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred in the main menu: {e}")
        finally:
            print("Main menu operation completed.")

if __name__ == "__main__":
    main()