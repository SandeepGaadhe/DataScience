import os

class Circle(object):
    
    no_of_circles = 0
    
    def __init__(self, radius):
        self.__radius = radius
        Circle.no_of_circles += 1

    @staticmethod
    def getPi():
        return float(3.14)
    
    @staticmethod
    def square(x):
        return x**2
    def area(self):
        return (Circle.getPi())*self.square(self.__radius)
    @classmethod
    def getCircleCount(self):
        return Circle.no_of_circles

res_lst = list()
lst = list(map(lambda x: float(x.strip()), input().split(',')))
for radius in lst:
    c = Circle(radius)
    res_lst.append( str(c.getCirclesCount()) + ":" + str(c.area()))
print(f"{str(res_lst)}\n{str(Circle.getCirclesCount())}" )


print('\n\n\n\n\n----------------------------')        
print(res_lst)
print(str(Circle.no_of_circles))
print(Circle.getCirclesCount())
print('\n\n\n\n\n')

#r = []
#r = input("Enter rad list : ")
#

#area = []
#for i in r:
#    try:
#        i = int(i)
##        print(i)
#        c1 = Circle(i)
#        area.append(c1.area())
#    except ValueError:
#        pass
#
#print(area)
#print(len(area))


    
    
#if __name__ == "__main__":
#    
#    #with open(os.environ['OUTPUT_PATH'], 'w') as fout:
#    with open('S:\SandeepG\Official\DataScience\Fresco\OUT.TXT', 'w') as fout:
#        res_lst = list()
#        lst = list(map(lambda x: float(x.strip()), input().split(',')))
#        for radius in lst:
#            res_lst.append(Circle(radius).area())
#        fout.write("{}\n{}".format(str(res_lst), str(Circle.no_of_circles)))
