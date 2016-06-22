import cluster
import random
import pandas as pd

class Kmeans :
    K = 1
    points = []
    clusters = []
    centroids = []
    num = 0
    
    lastClusters = []
    def __init__(self, points, n):
        self.K = n
        self.points = points
        for i in xrange(n):
            self.clusters.append([])
        self.centroids = []
        self.num = len(points)
        self.lastClusters = []
    def cluster(self):
        self.num = len(self.points)
        centroids_points = random.sample(self.points, self.K)
        self.centroids = [p.coord for p in centroids_points]
        self.reclust()
        # print "LA", self.lastClusters
        # print "CU", self.clusters
        counter = 1
        while self.isChanged():
            self.reclust()
            print "Round-" + str(counter)
            counter += 1
            # print "LA", self.lastClusters
            # print "CU", self.clusters
            # print "CENTROIDS", self.centroids
        
    def reclust(self):
        self.lastClusters = []
        for i in range(len(self.clusters)):
            self.lastClusters.append(self.clusters[i][:])
        for i in self.clusters:
            self
        self.clusters = []
        for i in xrange(self.K):
            self.clusters.append([])
        for pi in self.points:
            distances = [pi.eu_dist(pi.coord, self.centroids[i]) for i in xrange(self.K)]
            num_cluster = distances.index(min(distances))
            self.clusters[num_cluster].append(self.points.index(pi))
        self.centroids = []
        for c in self.clusters:
            pcen = []
            ps = []
            for i in c:
                ps.append(self.points[i].coord)
            df = pd.DataFrame(ps)
            length = len(df.iloc[0])
            for i in xrange(length):
                pcen.append(df.iloc[:,i].mean())
            self.centroids.append(pcen)
            
    def isChanged(self):
        for i in xrange(self.K):
            if sorted(self.clusters[i]) != sorted(self.lastClusters[i]):
                return True
        return False
            
    def getPoints(self):
        cluster = []
        for c in self.clusters:
            cluster.append([])
        for c in self.clusters:
            for i in c:
                cluster[self.clusters.index(c)].append([self.points[i].coord, self.points[i].tag])
        return cluster
     
    def getTag(self):
        tag = []
        cluster = self.getPoints()
        for group in cluster:
            vote = []
            for i in xrange(self.K):
                vote.append(0)
            for fig in group:
                vote[fig[1]] += 1
            tag.append(vote.index(max(vote)))
        return tag
    
    
if __name__ == '__main__':
    ps = []
    ps.append(cluster.Point([0]))
    ps.append(cluster.Point([1]))
    ps.append(cluster.Point([2]))
    ps.append(cluster.Point([3]))
    ps.append(cluster.Point([4]))
    ps.append(cluster.Point([5]))
    ps.append(cluster.Point([6]))
    ps.append(cluster.Point([7]))
    ps.append(cluster.Point([8]))
    ps.append(cluster.Point([9]))
    

    kms = Kmeans(ps, 2)
    kms.cluster()
    # print kms.clusters
    cluster = []
    for c in kms.clusters:
        cluster.append([])
    for c in kms.clusters:
        for i in c:
            cluster[kms.clusters.index(c)].append(ps[i].coord)
    # print cluster
    kms.clusters = [[2,4,7,8]]
    kms.lastClusters = [[2,4,7,8,2,4,7,8]]
    print kms.isChanged()
    