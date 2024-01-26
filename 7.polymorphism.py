#polymorphism without inheritence
class India:
    def capital(self):
        print('New Delhi is captial of india')
    def language(self):
        print('hindi is the national language of india')

class USA:
    def capital(self):
        print('Washington, D.C is captial of india')
    def language(self):
        print('engilsh is the national language of USA')


a=India()
a.capital()     #returns 'New Delhi is captial of india'
a.language()    #returns 'hindi is the national language of india'

b=USA()
b.capital()     #returns 'Washington, D.C is captial of india'
b.language()    #returns 'engilsh is the national language of USA'



#polymorphism with inheritence called overriding
class Bird:          #creating class Bird
    def intro(self):
        print('There are many types of birds')

    def flight(self):
        print('Most of the birds can fly but some cannot')

class sparrow(Bird):    #child class of Bird
    def flight(self):
        print('sparrow can fly')

class ostrich(Bird):     #child class of Bird
    def flight(self):
        print('ostriches cannot fly')

a=Bird()       #calling bird with object 'a'
a.intro()      #returns 'There are many types of birds'
a.flight()     #returns  'Most of the birds can fly but some cannot'

b=sparrow()    #calling sparrow with object 'b'
b.intro()      #returns 'There are many types of birds'
b.flight()     #returns 'sparrow can fly'

c=ostrich()     #calling ostrich with object 'c'
c.intro()       #returns 'There are many types of birds'
c.flight()      #returns 'ostriches cannot fly'
