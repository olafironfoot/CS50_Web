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

    """docstring for Flight."""
    counter = 1

    def __init__(self):
        self.id = Flight.counter
        Flight.counter += 1

        self.passengers = []


#creating a function that adds Passengers
    def add_passenger(self, p):
        self.passengers.append(p)
        p.flight_id = self.id
        #p.flight_id = Flight.counter


    def print_info(self):
        # for passenger in self.passengers:
        #     print(f"Passenger name: {passenger.name} \n Flight ID: {passenger.flight_id}")

        print(self.passengers)


        #Question: Why doesn't print(self.passengers) work like print(list) below? print(self.passengers) returns a memory address instead of a list. 

        #Question1(Answered1), if both are list, why does one return the list and the other the memory address?
        #because the list was in the function, "print_info" under the class flight. when moved to the main code, it was able to print the list.
        #in order to print the list self.passengers


        #Question: how to print the "self.passengers = []" list?
        # print(f"Passenger name: {self.passengers} \n Flight ID: {passengers.flight_id}")

#recreating class
class Passenger:

    def __init__ (self, name):
        self.name = name

#after all definitions, execute the code

def main():

    f1 = Flight()
    michael = Passenger(name = "MichaelScott")
    f1.add_passenger(michael)
    f1.print_info()

    list = [1, 2, 3]
    print(list)




if __name__ == "__main__":
    main()
