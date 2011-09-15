#! /usr/bin/python

'''
    RoadRater is a tool to rate the "fun-ness" of roads. The end goal is to
    find the most fun road <pause> in the world. The metrics used to measure
    "fun-ness" are in the metrics class. Road data comes from the open street
    map project.
'''
import metric

class RoadRater:
#    oRoad

#    def __init__(self, road):
#        self.oRoad = road

    '''
        Rate takes a list of waypoints as a road and runs metrics to determin
        the "fun-ness"
    '''
    def rate(self, liRoad):
        print 'Entering RoadRater.rate'
        results = {}
        # The results of metrics are normalized to 100
        results['Twistyness'] = metric.Metric.twistsPerMile(liRoad)
        results['Remoteness'] = metric.Metric.distanceFromCiv(liRoad)

        print 'Leaving RoadRater.rate'
        return results


    def findRoad(self, sRoadName):
        print 'Entering RoadRater.findRoad'
        liRoad = []
        # TODO

        print 'Leaving RoadRater.findRoad'
        return liRoad


    def run(self, sRoadName):
        print 'Entering RoadRater.run'
        # Find the road name in the database, parse it into a road list
        liRoad = self.findRoad(sRoadName)

        results = self.rate(liRoad)

        print 'Leaving RoadRater.run'
        return results

def main():
    results = RoadRater()
    results.run("Hello World")

    print results


main()
