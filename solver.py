#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
from collections import namedtuple

import numpy as np

Point = namedtuple("Point", ['x', 'y'])

#각 edge들의 거리에 관한 리스트를 리턴하는 함수
def LenofEdges(solution, points, nodeCount):
    LengthofEachRoute = [0]*nodeCount
    
    for index in range(0, nodeCount-1):
        LengthofEachRoute[index] = length(points[solution[index]], points[solution[index+1]])
    LengthofEachRoute[-1] = length(points[solution[-1]], points[solution[0]])
    
    return LengthofEachRoute


# calculate the length of the tour
def CalculateObj(points, solution, nodeCount):
    obj = length(points[solution[-1]], points[solution[0]])
    for index in range(0, nodeCount-1):
        obj += length(points[solution[index]], points[solution[index+1]])

    return obj

#어떤 노드에서 가장 가까이에 있는 노드를 리턴해준다.
def NodeofNearest(points, SwappingPoint, nodeCount):
    #일단 입력받은 노드에서 각 노드간의 거리를 계산한 뒤 리스트에 넣는다.
    minvalue = 0
    minnode = 0
    
    for i, point in enumerate(points):
        tempvalue = length(point, points[SwappingPoint])
        #print "tempvalue: ", tempvalue
        if( minvalue is 0 and tempvalue > 0):
            #print "minvalue is 0 and tempvalue is not 0"
            minvalue = tempvalue
            minnode = i 
        if( minvalue > tempvalue and tempvalue > 0):
            #print "minvalue > tempvalue"
            minvalue = tempvalue
            minnode = i    

    #print "minvalue: ", minvalue, " minnode: ", minnode
    
    return minnode
    

# 가장 현재식에서 가장 거리가 긴 루트를 찾아, 그 인덱스를 리턴한다.

def IndexofMaxLengthRoute( LengthofEachRoute ):
    return LengthofEachRoute.index(max(LengthofEachRoute))

def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    nodeCount = int(lines[0])

    points = []
    for i in range(1, nodeCount+1):
        line = lines[i]
        parts = line.split()
        points.append(Point(float(parts[0]), float(parts[1])))

    # build a trivial solution
    # visit the nodes in the order they appear in the file
    solution = range(0, nodeCount)
    
    # 임시 값을 넣어둘 리스트
    tempsolution = solution
    
    # 각 node에서 다음 node까지의 거리리스트
    #LengthofEachRoute = [0]*nodeCount
    
    # calculate the length of the tour
    obj = CalculateObj(points, solution, nodeCount)
    #LengthofEachRoute = LenofEdges(solution, points, nodeCount)
        
    # node 갯수만큼 루프를 돌리면서 최적해를 찾아본다.
    for i in solution:
        # 가장 거리가 긴 루트를 찾고 인덱스를 뽑아온다.   
         
        SwappingPoint1 = i
    
        # 그 node에서 가장 짧은 거리에 있는 node를 찾아본다.
        SwappingPoint2 = NodeofNearest(points, SwappingPoint1, nodeCount)
    
        #
        #print "Swapping Point 1: ", SwappingPoint1, " Swapping Point 2: ", SwappingPoint2
        #서로 바꿔준다.
        tempindex1 = solution.index(SwappingPoint1)
        tempindex2 = solution.index(SwappingPoint2)
        
        tempsolution[tempindex1] = SwappingPoint2
        tempsolution[tempindex2] = SwappingPoint1
    
        tempObj = CalculateObj(points, tempsolution, nodeCount)
        
        if tempObj < obj:
            solution = tempsolution
            #LengthofEachRoute = LenofEdges(solution, points, nodeCount)
            obj = CalculateObj(points, solution, nodeCount)
    # 다시 계산
    #obj = length(points[solution[-1]], points[solution[0]])
    #for index in range(0, nodeCount-1):
        #obj += length(points[solution[index]], points[solution[index+1]])
        #LengthofEachRoute[index] = length(points[solution[index]], points[solution[index+1]])
    #LengthofEachRoute[-1] = length(points[solution[-1]], points[solution[0]])
    
    
    # prepare the solution in the specified output format
    output_data = str(obj) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, solution))

    return output_data


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/tsp_51_1)'

