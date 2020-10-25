import pickle
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

def Choose_File():
    file_handle = False
    File_Name = input("choose a file name: ")
    if (File_Name == ""):
        File_Name = 'DataBase.Dat'
    password = input("password for that file: ")
    encryptor = get_encrypt(password)
    while (not file_handle):
        file_handle = open_file(File_Name)
        if (not file_handle):
            NoFile = input ("File does not exist. Do you want to try again or create a blank file?.\n1 = try again\n2 = create a new file")
            if (NoFile == "1"):
                File_Name = input("Re-type filename: ")
                password = input("Re-type password: ")
            elif (NoFile == "2"):
                file_handle = open_file(File_Name, force=True, encryptor=encryptor)

    return ([File_Name, file_handle, password, encryptor])

def Normal():

    (File_Name, fileHandle, password, encryptor) = Choose_File()
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

    os.chdir(input("specify data directory: "))
    Normal()