import os


class Circle(object):
    
    no_of_circles = 0
    
    def __init__(self, radius):
        self.__radius = radius
        Circle.no_of_circles += 1
        
    @staticmethod
    def square(x):
        return x**2
    def area(self):
        return 3.14*self.square(self.__radius)
    def getCirclesCount(self):
        return Circle.no_of_circles

res_lst = list()
lst = list(map(lambda x: float(x.strip()), input().split(',')))
for radius in lst:
    res_lst.append(Circle(radius).area())


        
print(res_lst)
print(str(Circle.no_of_circles))
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
