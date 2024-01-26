#Inheritence is used to inherit methods from one class
class livingthings:
    def plants(self):
        print('Plants are living things')
    def humans(self):
        print('humans are living things')

class properties(livingthings):  #creating class 'properties' with inheritence the properties of 'livingthings' class
    def breathe(self):
        print('plants breathe co2')
    def plants(self):            #overriding the plants method
        print('Plants  take water, co2')
a=livingthings()         #calling the 'livingthings' class
a.plants()               #returns 'Plants are living things'
a.humans()               #returns 'humans are living things'

b=properties()           #calling the 'properties' class
b.plants()               #returns 'plants take water, co2'
b.humans()               #returns 'humans are living things'
b.breathe()              #returns 'plants breathe o2'
