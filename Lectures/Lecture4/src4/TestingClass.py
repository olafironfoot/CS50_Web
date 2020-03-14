class User:
    def __init__ (self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday

#Can assign a variable to store infomation within a class User()
Thisperson = User("Dave", 192832)

print(Thisperson.name, Thisperson.birthday)

#this needs to be assigned, otherwise just spits out the memory space it's stored
print(User("blah", 123891))

#def __repr__(self):
#    return "<__main__.User: =" + str(self.full_name) + ">"
