# inheritance when using constructor
class Bird:                 #creating class 'Bird'
    def __init__(self,name):      #init constructor
        self.name=name
    def getname(self):            # method 'getname'
        print(f'{self.name} can fly')


class Color(Bird):         # child class of Bird
    def __init__(self,name,color):
        self.color=color
        Bird.__init__(self,name)    #invoking the __init__ of Bird class
    def getcolor(self):
        print(f'{self.name} is in {self.color}')

d=Bird('Owl')     #calling the 'data' parent class with object 'd' and parameter 'owl'
d.getname()    #returns 'owl can fly'

t=Color('owl','black')     #calling the child class 'Color' with object 't' and paramaneter 'black'
t.getname()        #returns 'owl can fly'
t.getcolor()        #returns 'owl is in black color'
