class Person:
    def __init__(self, name: str):
        self.name = name


class Partner(Person):
    def __init__(self, name: str, bike: list):
        """
        Here I instantiate 'Partner' Objects!
        """
        # super().__init__()
        self.name = name
        self.bike = bike


class Client(Person):
    def __init__(self, name: str):
        """
        Here I instantiate 'Client' Objects!
        """
        # super().__init__()
        self.name = input("Give your name")
        print(f"Welcome {self.name}! How would you like to search for a bike?!")
        print("1. By age")
        print("2. By manufacturer")
        print("3. List Type")
        print("0. Exit")
        self.bikeselection = input("Type an option: ")
        choose_bike(self.bikeselection)

    def choose_bike(self, bikeoption):
        self.bikeoption = bikeoption
        while option != 0:
            if option == 1:
                usr_desired_age = input("Enter the desired bike age")
                bike for bike in bikes:
                    if usr_desired_age == bike.age
                        print(bikes[bike])

            elif option == 2:
                pass
            elif option == 3:
                pass



"""
        for i in
        self.bikeselection
        if bikeselection
        self.bike
"""

class Bike():
    def __init__(self, number, modelname, owner, age, manufacturer, type_):
        self.modelname = modelname
        self.owner = owner
        self.age = age
        self.manufacturer = manufacturer
        self.type_ = type_
        self.number = number

    def __repr__(self):
        return f'Bike{self.number}: {self.modelname},\nType: {self.type_},\nManufacturer: {self.manufacturer},\nAge of bike: {self.age},\nOwner: {self.owner}\n'



class RentManagement:
    def __init__(self, partners_management, clients_management):
        self.bicyclestatus = 'Available'
        self.activerents = []
        self.oldbills = []

        pass

    def rent(self):
        pass

    def return_bycicle(self):
        # mark the bicycle  as AVAILABLE
        # mark the bill as CLOSED
        # .append to a list with CLOSED BILLS
        pass

    def bycicles_list(self):
        # read from db.py thn LISTA me ta podhlata???
        pass

class ClientManagement:
    # write to db.py -> a new CLIENT OBJECT to the CLIENTS LIST
    # return what???
    pass


class PartnerManagement:
    # write to db.py -> a new PARTNER OBJECT to the PARTNER LIST
    pass
