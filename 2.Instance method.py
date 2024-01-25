#example for class attribute and instance method
#creating class as country and instance method as primeminister

class country:   #creating class as country
    countryname='India'    #class attribute

    def primeminister(self): #instance method

        print('Prime minister of India is narendra modi')

a=country()     #calling conutry class
print(a)        #returns memory of object 'a'
print(a.countryname)    #returns class attribute 'India'
a.primeminister()    #returns 'Prime minister of India is narendra modi



