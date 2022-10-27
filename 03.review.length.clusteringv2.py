import json
import re

data_file = open("/media/leon/MCU/USTH/Data mining/DataMining data/yelp_academic_dataset_review.json")

class cluster:
    def __init__(self, *points):
        self.points = []

    def __del__(self):
        return None

    def add_points(self, point):
        self.points.append(point)

    def merger_clusters(self, points):
        self.points = self.points + list(points)

    def min_distance_cal(self, cluster):
        distance = None
        for i in self.points:
            for j in cluster.points:
                if i - j != 0:
                    distance = abs(i - j)
        return(distance)


    def printpoint(self):
        for i in self.points:
            print(self.points[i].length)



data_file = open("/media/leon/MCU/USTH/Data mining/DataMining data/yelp_academic_dataset_review.json")


clusterlist = []
for i, line in enumerate(data_file):
    x = json.loads(line)['text']
    c = cluster()
    c.add_points(len(x))
    clusterlist.append(c)
    if i>10:
        break

distancelist = []
for i in range(len(clusterlist)):
    for j in range(len(clusterlist)):
        x = clusterlist[i].min_distance_cal(clusterlist[j])
        distancelist.append(x)

#for i in distancelist:

print(distancelist)
