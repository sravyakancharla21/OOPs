class Data:
    def __init__(self,data):
        self.data=data
    def getData(self):
        print(f'data:{self.data}')


class time(Data):
    def getTime(self):
        print(f'Time:{self.data}')

d=Data(20)
d.getData()

t=time(30)
t.getData()
t.getTime()
