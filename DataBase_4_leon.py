import pickle
import time


def First_Time():
    choice = input('Type first thing to add to database')
    DataBase = [choice]
    while choice != 'DONE':
        choice = input('type next item to add to database, if finished type DONE')
        if choice != 'DONE':
            DataBase.append(choice)
            


    
    pickle.dump(DataBase, open('DataBase.Dat','wb'))
    
    print('done')
    time.sleep(9)
    raise
        




def Normal():
    while True:
        DataBase = pickle.load(open('DataBase.Dat','rb'))
        
        print("Do you want to")
        print("1. View Database")
        print("2. Add to the Database")
        print("3. Delete items")
        print("")
        print(" type 1 2 or 3")
        choice = input('')
        
    
        if int(choice) == 1:
            
            print(DataBase)

        elif int(choice) == 2:
            choice = input('Type first thing to add to database')
            DataBase.append(choice)
            while choice != 'DONE':
                choice = input('type next item to add to database, if finished type DONE')
                if choice != 'DONE':
                    DataBase.append(choice)



        elif int(choice) == 3:
            print(DataBase)
                 
            
            print("")
            print("")
            print("Which Item to delete? Enter name")
            choice = input("")
            
            
            
            DataBase.remove(choice)
            
                






            
        pickle.dump(DataBase, open('DataBase.Dat','wb'))    






            

code = input("Hi Leon, Enter Activation Code:")

if code == "374389473084738":
    First_Time()

elif code == "NMDiFgdh8":
    Normal()

else:
    code = input("wrong")
    
