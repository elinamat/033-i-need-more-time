from rent import PartnerManagement
from rent import ClientManagement
from rent import RentManagement
from rent import Partner
from rent import Client
from rent import Bike
# import rent.Bike as Bike
# from db import partners
# from db import bikes
#from db import *
import pickle


def main_menu():
    print("1. Rent a Bike")
    print("2. Return a Bike")
    print("3. List Bikes")
    print("4. List Bills")
    print("5. Incoming Report")
    print("0. Exit")
    opt = int(input("Type an option >> "))
    return opt


if __name__ == '__main__':

    # bike1 = # TODO
    #John = Partner()
    #John.name = John

    """ ----> MATHIAAAAAAAAS!!!  HELP - WHY IT ISN'T WORKING ????????????? <----
    GOAL: Creating PARTNER Objects from a list inside db.py file
    check globals() locals() or exec()
    """
    # mypartners = []
    # for partner in partners:
    #     partner = Partner()
    #     mypartners.append(partner)
    #     # partners[partner] = Partner()
    #     #    = Partner()
    #     #print(mypartners[partner])  # prints the name??!! no
    #     print(mypartners[partner].type)  # prints the type(object)??!! no

    bike1 = Bike(1,"Peugeot 3K", partners[0], 2, "Peugeot", "City Bike", "Available")
    bike2 = Bike(2,"KTM 3000", partners[1], 4, "KTM", "Mountain Bike", "Available")
    bike3 = Bike(3,"VanMoof S3", partners[2], 1, "VanMoof", "Electric Bike", "Available")
    bike4 = Bike(4, "OLE 40000", partners[3], 1, "OLE", "City Bike", "Available")
    bike5 = Bike(5, "CB 2015", partners[2], 7, "Cruzbike", "City Bike", "Available")
    bike6 = Bike(6, "Cube 7000", partners[4], 3, "CUBE", "Mountain Bike", "Available")
    bike7 = Bike(7, "Ampler Curt Urban", partners[5], 5, "Ampler Curt", "Electric Bike", "Available")
    bike8 = Bike(8, "Genesis 150Hb", partners[5], 6, "Genesis", "Mountain Bike", "Available")
    # TODO:
    """
    Create bike objects using dynamic list variable names!? 
    (with two for-loops and user inputs for the bike arguments)
    for example:
    for x in range(0, 8):
    globals()['string%s' % x] = 'Hello'
    # string0 = 'Hello', string1 = 'Hello', ... string7 = 'Hello',
    """

    bikelist = [bike1, bike2, bike3, bike4, bike5, bike6, bike7, bike8]
    # or use bikelist.append(Bike("Peugeot 3K", partners[0], 2, "Peugeot", "City Bike"))
    """    
    temp = open("temp", "wb")
    with open("db.py", "a+") as f:
        # TODO - APPEND TO LIST IS NOT WORKING
        # pickle.dump(bikelist, fdb)
        for line in f:
            if line.startswith("bikes"):
                line = bikelist
                # for item in bikelist:
                #   bikes.append(item)]
    temp.close()
    """
    partners_management = PartnerManagement()
    clients_management = ClientManagement()
    rent_management = RentManagement(partners_management, clients_management)

    option = -1
    while option != 0:

        option = main_menu()

        if option == 1:
            name = input("Give your name: ")
            new_client = Client(name)
            print(f"Welcome {new_client.name}! How would you like to search for a bike?!")
            print("1. By age")
            print("2. By manufacturer")
            print("3. List Type")
            print("0. Exit")
            bikeselection = int(input("Type an option: "))
            rent_management.rent_bike(bikeselection)
        elif option == 2:
            rent_management.return_bycicle()
        elif option == 3:
            print(rent_management.bycicles_list())
        elif option == 4:
            print(rent_management.bills_list())
        elif option == 5:
            print(rent_management.report())
