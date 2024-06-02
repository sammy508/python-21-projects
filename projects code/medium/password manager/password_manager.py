

from cryptography.fernet import Fernet
import os



def generate_key():
    # Generate a key
    key = Fernet.generate_key()
    # Save the key to a file
    with open("key.key", 'wb') as key_file:
        key_file.write(key)
    print("Key generated and saved to 'key.key'.")

def load_key():
    try:
        
        if not os.path.exists("key.key"):
            print("Key file not found. Generating a new key...")
            generate_key()
        
        with open("key.key", 'rb') as file:
            key = file.read()
            return key
    except Exception as e:
        print(f"An error occurred while loading the key: {e}")
        return None

key = load_key()
fer = Fernet(key)

def view():
    try:

         with open('password.txt','r') as file:
            for line in file.readlines():
                data = line.rstrip()
                username,password =data.split()
                print(f"user: {username}, | password: {fer.decrypt(password.encode()).decode()}")
    except Exception as e:
        print(f"you got an error{e}")
  
   

def add():
    name = input("User Name: ")
    password = input("Enter Password: ")
    encrypted_password = fer.encrypt(password.encode()).decode()
    try:
        with open('password.txt','a')as file:
            file.write(f"{name}|{encrypted_password}\n")
    except Exception as e:
        print(f"An error occurred: {e}")        

while True:
    mode = input("Would you like to add new password or view exsiting one.(add , view), press q to quit?").lower()

    if mode == "q":
        quit()
    elif mode == "view":
        view()

    elif mode == "add":
        add()
    else:
        print("You have entered invalid modes")   
        continue     

# from cryptography.fernet import Fernet
# import os

# def generate_key():
#     # Generate a key
#     key = Fernet.generate_key()
#     # Save the key to a file
#     with open("key.key", 'wb') as key_file:
#         key_file.write(key)
#     print("Key generated and saved to 'key.key'.")

# def load_key():
#     try:
        
#         if not os.path.exists("key.key"):
#             print("Key file not found. Generating a new key...")
#             generate_key()
        
#         with open("key.key", 'rb') as file:
#             key = file.read()
#             return key
#     except Exception as e:
#         print(f"An error occurred while loading the key: {e}")
#         return None

# key = load_key()

# if key is None:
#     print("Exiting program due to missing or corrupted encryption key.")
#     exit()

# fer = Fernet(key)

# def view():
#     try:
#         with open('password.txt', 'r') as file:
#             for line in file.readlines():
#                 data = line.rstrip()
#                 username, encrypted_password = data.split("|")
#                 password = fer.decrypt(encrypted_password.encode()).decode()
#                 print(f"User: {username} | Password: {password}")
#     except FileNotFoundError:
#         print("Error: The password file was not found.")
#     except Exception as e:
#         print(f"An error occurred while reading passwords: {e}")

# def add():
#     name = input("User Name: ")
#     password = input("Enter Password: ")
#     encrypted_password = fer.encrypt(password.encode()).decode()
#     try:
#         with open('password.txt', 'a') as file:
#             file.write(f"{name}|{encrypted_password}\n")
#     except Exception as e:
#         print(f"An error occurred while writing to the password file: {e}")

# while True:
#     mode = input("Would you like to add a new password or view an existing one (add, view)? Press q to quit: ").lower()
#     if mode == "q":
#         break
#     elif mode == "view":
#         view()
#     elif mode == "add":
#         add()
#     else:
#         print("You have entered an invalid mode. Please enter 'add' or 'view'.")

