# class User:
#     def __init__ (self, full_name, birthday):
#         self.name = full_name
#         self.birthday = birthday
#
# #Can assign a variable to store infomation within a class User()
# Thisperson = User("Dave", 192832)
#
# print(Thisperson.name, Thisperson.birthday)
#
# #this needs to be assigned, otherwise just spits out the memory space it's stored
# print(User("blah", 123891))

#def __repr__(self):
#    return "<__main__.User: =" + str(self.full_name) + ">"



class Flight:
    pass
    counter = 1

    def __init__(self):
        self.id = Flight.counter
        Flight.counter += 1

        self.passengers = ["self.passangers list 1", "self.passangers list 2"]


    def add_passenger(self, p):
        self.passengers.append(p)
        p.flight_id = self.id

    def print_info(self):

        print(self.passengers)
        # print(self.passengers.flight_id)

        #Question 1: Why doesn't print(self.passengers) work like print(list) below? print(self.passengers) returns a memory address instead of a list.
        #Question 2: how do we print the flight_id? because print(self.passengers.flight_id) doens't seem to work..

#recreating class
class Passenger:

    def __init__ (self, name):
        self.name = name

#after all definitions, execute the code

def main():

    f1 = Flight()
    michael = Passenger(name = "MichaelScott")      #creates an object under the class Passenger
    f1.add_passenger(michael)       #calls the function add_passenger(for the flight, f1) passing the value, michael- which is an object under the class Passenger)
                                    #the function appends michael into the f1.passenger list
    f1.print_info()                 #prints the attributes for the object f1, namely the list f1.passengers

    list = [1, 2, 3]
    print(list)




if __name__ == "__main__":
    main()
