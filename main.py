from account import *
import os
import json

print("Welcome to the Bank Manager")

x = False
while not x:
    main_response = int(input("\nSelect one of the following options:\n"
                              "1. List Accounts\n"
                              "2. Edit Balance\n"
                              "3. Add Account\n"
                              "4. Edit Account\n"
                              "5. Delete Account\n"
                              "6. Exit Program\n\n"))

    # Listing all accounts
    if main_response == 1:
        with open('accounts.json') as f:
            accounts = json.load(f)
            number_of_accounts = len(accounts['accounts'])
        if number_of_accounts == 0:
            print("There are no accounts to list.")
        else:
            with open("accounts.json") as f:
                data = f.read()

            print(data)

    # Depositing/Withdrawing
    elif main_response == 2:
        balance_update = int(input("Please select one of the following options:\n"
                                   "1. Deposit\n"
                                   "2. Withdraw\n\n"))

        if balance_update == 1 or balance_update == 2:
            account_number = int(input("Please enter your account number: "))
            with open('accounts.json', 'r+') as file:
                file_data = json.load(file)
                # Make a list of account numbers
                numbers = []
                for account in file_data['accounts']:
                    ID = account['accountID']
                    numbers.append(ID)
                # Check if account exists
                if account_number in numbers:
                    # Loop through all accounts and update the specified one
                    for account in file_data['accounts']:
                        if account['accountID'] == account_number:
                            if balance_update == 1:
                                deposit_amount = int(input("Please enter the amount you wish to deposit: "))
                                print(account['balance'])
                                account['balance'] += deposit_amount
                                print(account['balance'])
                                file.seek(0)
                                json.dump(file_data, file, indent=4)
                            elif balance_update == 2:
                                withdraw_amount = int(input("Please enter the amount you wish to withdraw: "))
                                account['balance'] -= withdraw_amount
                                file.seek(0)
                                json.dump(file_data, file, indent=4)

                else:
                    print("The account number you entered cannot be found.\n"
                          "Returning to the main menu...\n")

        # Invalid Selection
        else:
            print("You have made an invalid selection.\n"
                  "Returning to the main menu...\n")


    # Adding a new account
    elif main_response == 3:
        with open('accounts.json') as f:
            accounts = json.load(f)
            number_of_accounts = len(accounts['accounts'])
            if number_of_accounts == 0:
                maxID = 1
            else:
                maxIDaccount = max(accounts['accounts'], key=lambda ev: ev['accountID'])
                maxID = maxIDaccount['accountID'] + 1

        account_ID = maxID
        first_name = input("Please enter your first name: ")
        last_name = input("Please enter your last name: ")
        starting_balance = int(input("Please enter an initial deposit (initial balance amount): "))
        new_account = Account(account_ID, first_name, last_name, starting_balance)
        # Converting to dict
        new_account_dict = new_account.__dict__
        # Writing to accounts.json
        with open('accounts.json', 'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Add information about new account to the list of JSON objects in accounts.json
            file_data["accounts"].append(new_account_dict)
            # Sets file's current position at offset.
            file.seek(0)
            # Converting to JSON format and adding to file
            json.dump(file_data, file, indent=4)



    # Editing an account
    elif main_response == 4:
        account_number = int(input("Please enter your account number: "))
        with open('accounts.json', 'r+') as file:
            file_data = json.load(file)
            # Make a list of account numbers
            numbers = []
            for account in file_data['accounts']:
                ID = account['accountID']
                numbers.append(ID)
            # Check if account exists
            if account_number in numbers:
                # Loop through all accounts and update the specified one
                for account in file_data['accounts']:
                    if account['accountID'] == account_number:
                        updated_first_name = input("Please enter the correct first name: ")
                        updated_last_name = input("Please enter the correct last name: ")
                        account['firstName'] = updated_first_name
                        account['lastName'] =updated_last_name
                        file.seek(0)
                        json.dump(file_data, file, indent=4)

            else:
                print("The account number you entered cannot be found.\n"
                      "Returning to the main menu...\n")

    # Deleting an account
    elif main_response == 5:
        del_account_number = int(input("Please enter your account ID: "))
        confirmation = input("Are you sure you want to delete this account (y/n)? ")
        if confirmation == 'Y' or confirmation == 'y':
            with open('accounts.json', 'r+') as file:
                file_data = json.load(file)
                # Make a list of account numbers
                numbers = []
                for account in file_data['accounts']:
                    ID = account['accountID']
                    numbers.append(ID)

            # Check if account exists
            if del_account_number in numbers:
                new_data = []
                for acc in file_data['accounts']:
                    if acc['accountID'] != del_account_number:
                        new_data.append(acc)

                file_data['accounts'].clear()
                file_data['accounts'] = new_data

                json.dumps(file_data)
                with open('accounts.json', 'w') as file:
                    file.seek(0)
                    json.dump(file_data, file, indent=4)

            else:
                print("The account number you entered cannot be found.\n"
                      "Returning to the main menu...\n")

        elif confirmation == 'N' or confirmation == 'n':
            print("Returning to the main menu...\n")

        else:
            print("You have made an invalid selection.\n"
                  "Returning to the main menu...\n")





    # Exit the program
    elif main_response == 6:
        print("\nThank you for using The Bank Manager\n"
              "Exiting program...")
        x = True
    else:
        print("\nInvalid selection.\n"
              "Returning to the main menu...")
