import pickle
import configparser
import time
import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

### password = b"password"
def get_encrypt(password):
    salt = b'\xd1\xe2[\xdd\x1c~#\xa4H6v\xfa\x8b1|\xd6'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(str.encode(password)))
    f = Fernet(key)
    return f

def open_file(File_Name, force=False, encryptor=False):
    if (not os.path.exists(File_Name)):
        if (force):
            write_file(File_Name, [], encryptor)
        else:
            return False

    try:
        file_handle = open(File_Name, "rb")
    except OSError:
        return False

    return file_handle

def write_file(File_Name, DataBase, encryptor):
    fh = open(File_Name, 'wb')
    fh.write(encryptor.encrypt(pickle.dumps(DataBase)))
    fh.close()

def Normal(File_Name):

    password = input("password for that file: ")
    encryptor = get_encrypt(password)

    fileHandle = open_file(File_Name)
    if (False == fileHandle):
        FailedToOpenFile = input("failed. did you mean %s or do you want to create a file with this name? (y/n): " % (File_Name))
        if ('y' == FailedToOpenFile):
            fileHandle = open_file(File_Name, force=True, encryptor=encryptor)
        if ('n' == FailedToOpenFile):
            os.exit(1)

    DataBase = pickle.loads(encryptor.decrypt(fileHandle.read()))
    fileHandle.close()

    while True:
        print("Do you want to")
        print("1. View Database\n2. Add to the Database\n3. Delete items")
        choice = input(" type 1, 2, or 3: ")

        if int(choice) == 1:
            print(DataBase)

        elif int(choice) == 2:
            choice = input('Type first thing to add to database ')
            DataBase.append(choice)
            while choice != 'DONE':
                choice = input('type next item to add to database, if finished type DONE ')
                if choice != 'DONE':
                    DataBase.append(choice)
            write_file(File_Name, DataBase, encryptor)

        elif int(choice) == 3:
            print(DataBase)
            choice = input("\n\nWhich Item to delete? Enter name ")
            DataBase.remove(choice)
            write_file(File_Name, DataBase, encryptor)

if __name__=="__main__":

    SecAcc = input("which database name do u want to open? ")
    config = configparser.ConfigParser()
    config.read("DataBase.ini")
    Normal(config.get(SecAcc, "file"))
