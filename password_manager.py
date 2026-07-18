import os

FILE_NAME = "passwords.txt"


def add_password():
    account = input("Enter Account Name: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{account},{username},{password}\n")

    print("\nPassword saved successfully!")


def view_passwords():
    if not os.path.exists(FILE_NAME):
        print("\nNo passwords found.")
        return

    print("\n========== Saved Passwords ==========")

    with open(FILE_NAME, "r") as file:
        data = file.readlines()

        if not data:
            print("No records found.")
            return

        for record in data:
            account, username, password = record.strip().split(",")
            print(f"\nAccount  : {account}")
            print(f"Username : {username}")
            print(f"Password : {password}")


def search_password():
    account_name = input("\nEnter Account Name to Search: ")

    if not os.path.exists(FILE_NAME):
        print("No passwords found.")
        return

    found = False

    with open(FILE_NAME, "r") as file:
        for record in file:
            account, username, password = record.strip().split(",")

            if account.lower() == account_name.lower():
                print("\nPassword Found!")
                print(f"Account  : {account}")
                print(f"Username : {username}")
                print(f"Password : {password}")
                found = True
                break

    if not found:
        print("\nAccount not found.")


def delete_password():
    account_name = input("\nEnter Account Name to Delete: ")

    if not os.path.exists(FILE_NAME):
        print("No passwords found.")
        return

    records = []
    found = False

    with open(FILE_NAME, "r") as file:
        for record in file:
            account, username, password = record.strip().split(",")

            if account.lower() != account_name.lower():
                records.append(record)
            else:
                found = True

    with open(FILE_NAME, "w") as file:
        file.writelines(records)

    if found:
        print("\nPassword deleted successfully!")
    else:
        print("\nAccount not found.")


def main():
    while True:
        print("\n========== Password Manager ==========")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Search Password")
        print("4. Delete Password")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            search_password()
        elif choice == "4":
            delete_password()
        elif choice == "5":
            print("\nThank you for using Password Manager!")
            break
        else:
            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    main()
