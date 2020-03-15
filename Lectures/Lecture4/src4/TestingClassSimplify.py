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


    def __init__(self):
        self.passengers = ["self.passangers list 1", "self.passangers list 2"]



    def print_info(self):

        print(self.passengers)


        #Question: Why doesn't print(self.passengers) work like print(list) below? print(self.passengers) returns a memory address instead of a list.


#recreating class
class Passenger:

    def __init__ (self, name):
        self.name = name

#after all definitions, execute the code

def main():


    f1.print_info()

    list = [1, 2, 3]
    print(list)




if __name__ == "__main__":
    main()
