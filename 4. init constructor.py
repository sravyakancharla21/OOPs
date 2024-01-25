# use of init constructor is to refresh the values(under init method) to default values once the object is created

class attendance:
    def __init__(self):
        self.count=0     #count will be '0' once the new object is created

    def attend(self):    #attend method is called once the student entered the class
        self.count+=1    #count is increased to 1 when student entered the class (When attend method is called)

    def presentstudents(self):     #presentstudents method is to return no of students are present
        print(self.count)

a=attendance()          #calling class attendance
a.presentstudents()     #returns '0'
a.attend()              #calling attend method when student entered the class
a.attend()
a.attend()
a.attend()
a.presentstudents()    #returns '4' beacuse we called attend method 4 times (four students attend the class)

#day 1 is completed we need to mark the attendance for next day so we are creating another object 'b' for counting the present students
b=attendance()
b.presentstudents()     #returns '0' because we didn't called attend method (no student attend the class yet)
b.attend()
b.attend()
b.attend()
b.attend()
b.attend()
b.presentstudents()     #returns '5' beacuse we called attend method 5 times (five students attend the class)