class Point :
    coord = []
    tag = 0
    def __init__(self, point, tag=0):
        self.coord = point
        self.tag = tag
    def show(self):
        print self.coord
    def eu_dist(self, p0, p1):
        length = len(p0)
        if length != len(p1):
            print "ERROR: length!"
            return False
        return sum([(p0[i] - p1[i]) ** 2 for i in xrange(length)])
    
    
    
    
    
if __name__ == '__main__' :
    p0 = Point([1, 4])
    p1 = Point([5, 4])
    print p0.eu_dist(p0.coord, p1.coord)