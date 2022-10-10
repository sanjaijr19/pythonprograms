class company:
    def companyname(self):
        return "Google"
class work(company):
    def bio(self):
        name=super().companyname()
        print("my name is ",name)
ob=work()
ob.bio()


class speed:
    def maxspeed(self):
        print("max sped is 200km/hr")
class fast(speed):
    def maxspeed(self):
        print("max speed is 10km/hr")
x=fast()
x.maxspeed()
y=speed()
y.maxspeed()



