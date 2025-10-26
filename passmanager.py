#passmanager.py
import getpass
import secrets
import string
import pyperclip
import logging
import re
import time
from masterauth import verify_master


from passstore import load_vault , save_vault

logging.basicConfig(
    filename="vault.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def generate_strong_password():
    length = int(input("Enter password length (min 12): "))
    if length < 12:
        print("Password too short! Must be at least 12.")
        return

    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    alphabet = string.ascii_letters + string.digits
    if include_symbols:
        alphabet += string.punctuation

    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    pyperclip.copy(password)
    print(f"\nGenerated password: {password}")
    print("(Copied to clipboard )")



  
def display_menu():
    print("1.add password      2.view password")
    print("3.modify password   4.delete service")
    print("5.Generate strong password   6.exit")

def main():
    if not verify_master():
     return

    vault = load_vault()
    print("current vault",vault)
   
    while True:
         
         display_menu()
         choice = input("enter : ")

         if choice == "1":
            service = input("enter service : ")
            if not re.match(r"^[A-Za-z0-9_-]{1,30}$", service):
             print(" Invalid service name! Use only letters, numbers, underscores, and hyphens (max 30 chars).")
             continue
            username = input("enter username : ")
            password = getpass.getpass("enter password :")
            vault[service] = {"user": username , "pass": password}
            save_vault(vault)
            logging.info(f"Added new service: {service}")

         elif choice == "2":
            if not vault :
                print("no entries found")
            else :
                for services , i in vault.items():
                    print(f"{services} -> user : {i['user']} | pass : {i['pass']}")

         elif choice == "3" :
             if not vault :
                 print(" no services")
             else:
                print("services saved in vault : ")
                for service in vault.keys():
                 print("-" , service)
                 
             service = input("Enter the service you want to modify: ")
             if service in vault:
              new_pass = getpass.getpass("Enter new password: ")
              vault[service]["pass"] = new_pass
              save_vault(vault)
              
              logging.info(f"Modified password for: {service}")
             else:
              print("Service not found.")
               

         elif choice == "4" :
             if not vault:
              print("No services to delete.")
             else:
              print("Services saved in vault:")
              for service in vault.keys():
               print("-", service)
        
             service = input("Enter the service you want to delete: ")
             if service in vault:
              del vault[service]
              save_vault(vault)
              
              logging.info(f"Deleted service: {service}")
             else:
              print("Service not found.")

         elif choice == "5":
           generate_strong_password()
     

         elif choice =="6":
            print("exiting.......")
            break
         else:
            print("invalid\n")

if __name__ == "__main__":
    main()
