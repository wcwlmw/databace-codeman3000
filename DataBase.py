import pickle
import time


def First_Time():
    choice = input('Type first thing to add to database ')
    passcode = input('Please type what you want your passcode to be ')
    DataBase = [choice]
    while choice != 'DONE':
        choice = input('type next item to add to database, if finished type DONE ')
        if choice != 'DONE':
            DataBase.append(choice)
            


    
    pickle.dump(DataBase, open('DataBase.Dat','wb'))
    
    print('done')
    time.sleep(9)
    raise
        


#this is incomplete, add way to name/rename file and platform/option list for databases

def Normal():
    File_Name = input("choose a file name: ")
    if (input == ""):
        File_Name = 'DataBase.Dat'
    try:
        file_handle = open(File_Name, 'wb')
        DataBase = pickle.load(file_handle)
    except OSError:
        print ("File does not exist. Creating blank.")
        DataBase = []
        file_handle = open(File_Name, "wb")
        pickle.dump(DataBase, file_handle)

    while True:


        
        print("Do you want to")
        print("1. View Database\n2. Add to the Database\n3. Delete items\n4. create file\n5. open file")
        print("")
        print(" type 1, 2, 3, 4, or 5")
        choice = input('')

    
        if int(choice) == 1:
            print(DataBase)

        elif int(choice) == 2:
            choice = input('Type first thing to add to database ')
            DataBase.append(choice)
            while choice != 'DONE':
                choice = input('type next item to add to database, if finished type DONE ')
                if choice != 'DONE':
                    DataBase.append(choice)

        elif int(choice) == 3:
            print(DataBase)
            
            print("")
            print("")
            print("Which Item to delete? Enter name ")
            choice = input("")

            DataBase.remove(choice)

        elif int(choice) == 4:


        pickle.dump(DataBase, open('DataBase.Dat','wb'))



code = input("Hi (imput user choice name here), Enter Activation Code:")

if code == "":
    First_Time()

elif code == passcode:
    Normal()

else:
    code = input("wrong")

    
