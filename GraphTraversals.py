import sys
# from queue import *
import Queue as Z
from multiprocessing import Queue

lines = []
intline = []
with open(sys.argv[2]) as f:
    # with open('input.txt',r) as f:
    #    lines.extend(f.read().splitlines())
    # with open(r'C:\Users\pslmo\Desktop\CSCI 561 AI\HW1_updated\testcases\t1.txt') as f:
    lines.extend(f.read().splitlines())
# lines.extend(f.read().splitlines())
# lines=f.read().splitlines()
# with open(sys.argv[2]) as f:
# lines.extend(f.read().splitlines())
fo = open("output.txt", "w")


def buildTree(v1, s2):
    dict_weights = dict()
    for v in s2:
        v2 = v.split('-')
        temp = dict()
        temp = {v2[0].strip(): v2[1]}
        dict_weights.update(temp)

    keysLst = dict_weights.keys()
    ##print '****'
    ##print keysLst

    return dict_weights


def BFS_Search(dict_Tree, sourceNode, targetNode, MaxFuel):
    # print "Inside BFS Search()"

    # print sourceNode+targetNode+MaxFuel
    S = sourceNode
    T = targetNode
    lastVisitedNode = ''
    fuelConsumed = 0
    # q = Queue(maxsize=0)
    # q.put((sourceNode,sourceNode,0))

    ##print "sdsfsdfdsgdfgfdhfghgh"+str(q.pop())
    lastNodeVisited = []
    # print "sourceNode-->"+S
    visitedNodes = []
    path = []
    # print "******"
    # print visitedNodes
    # sourceNode='D'
    ##print "size of queue"+str(q.qsize())
    # q.put('D')
    # q.put('A')
    edgesDict = dict()
    ##print "size of dictionary"+str(size(dict_Tree))
    # print "Visited Nodes Size()"
    # print len(visitedNodes)
    output = ''
    if (sourceNode == targetNode):
        remainingFuel = MaxFuel - fuelConsumed

        # print sourceNode+'-'+targetNode+' '+' '+remainingFuel
        output = sourceNode + '-' + targetNode + ' ' + ' ' + remainingFuel

    elif (sourceNode not in dict_Tree.keys()):
        # print'------- 1--------------'
        # print "No Path"
        output = "No Path"

    elif (targetNode not in dict_Tree.keys()):
        # print '------- 2--------'
        # print "No Path"
        output = "No Path"

    else:
        i = 0
        residualFuel = int(MaxFuel)
        # path.append(sourceNode)
        temp = 0
        output = ''
        # residualFuel=MaxFuel
        lastNodeVisited = ''
        lastEdgeWeight = 0
        finalNode = ''
        unableToReachTarget = False
        cummCost = 0
        output = ' '
        finalPath = ''
        totalCost = 0
        # print "inside else"
        q = Z.Queue(maxsize=0)
        q.put((sourceNode, sourceNode, 0))
        # print "qsizeoooooooooooooooooooooooooooooo"+str(q.qsize())
        while not q.empty():
            # print "-----------------------"
            # print str(dict_Tree)

            ##print "Queue-->"+str(q)
            v, path, cummCost = q.get()
            ##print "Vertex being expanded"+str(v)
            # print "path--->"+str(path)
            # print
            neighbours = dict()
            # print "&&&&&&&&&"+v
            if (v == targetNode and int(MaxFuel) >= int(cummCost)):
                # print "Path Found"+ path
                remainingFuel = int(MaxFuel) - int(cummCost)
                # print "remaining fuel-->"+str(remainingFuel)
                output = str(path) + ' ' + str(remainingFuel)
                # print "output"+str(output)
                finalPath = str(path)
                # print "finalPath--->"+finalPath
                return output

            if (v not in visitedNodes):

                edgesDict = dict_Tree.get(v)
                # print "neighbors--->"+str(edgesDict)
                visitedNodes.append(v)
                neighbors_vertices = edgesDict.keys()
                totalNeighbors = len(neighbors_vertices)
                # print "totalNeighbors---->"+str(totalNeighbors)
                # print "vertex being expanded now-->"+v
                # print sorted(edgesDict.keys())
                temp_queue = []
                # temp_queue.append(('B',10,15))
                # temp_queue.append(('A',20,30))
                # temp_queue.append(('C',50,12))
                # print "Sorted temp_queue-->"+str(sorted(temp_queue,reverse=False))
                targetNodeFound = False
                for key in sorted(edgesDict.keys()):
                    if key not in visitedNodes:
                        # print "inside if"

                        # fuelNeeded=int(MaxFuel)-(cummCost)
                        # weight=int(edgesDict[key])
                        totalFuel = cummCost + int(edgesDict[key])
                        # print "totalFuel-->"+str(totalFuel)+'MaxFuel'+str(MaxFuel)
                        if (int(MaxFuel) >= int(totalFuel)):
                            # print "node satified fuel condition"
                            if (key == targetNode):
                                finalPath = path + '-' + str(key)
                                totalCost = int(cummCost) + int(edgesDict[key])
                                remainingFuel = int(MaxFuel) - int(totalCost)

                            # temp_queue.append((key,path+'-'+str(key),cummCost+int(edgesDict[key])))
                            q.put((key, path + '-' + str(key), cummCost + int(edgesDict[key])))

                            ##print "sorted!!->"+str(temp_queue)
                            # for e1,e2,e3 in sorted(temp_queue,reverse=True):
                            # q.append((e1,e2,e3))

            # print"Queue after first traversal"
            ##print q
            ##print "queue after pop"+str(len(q))

            # break
            if (targetNodeFound == True):
                # print "time to return to parent function"+ str(finalPath)+str(remainingFuel)
                break

        if (finalPath == ''):
            # print "outbut-->"+output
            output = "No Path"
            # print "No path found!!!"

    return visitedNodes


def DFS_Search(dict_Tree, sourceNode, targetNode, MaxFuel):
    # print "Inside DFS Search()"
    # print sourceNode+targetNode+MaxFuel
    S = sourceNode
    T = targetNode
    lastVisitedNode = ''
    fuelConsumed = 0
    q = []
    q.append((sourceNode, sourceNode, 0))

    ##print "sdsfsdfdsgdfgfdhfghgh"+str(q.pop())
    lastNodeVisited = []
    # print "sourceNode-->"+S
    visitedNodes = []
    path = []
    # print "******"
    # print visitedNodes
    # sourceNode='D'
    # print len(q)
    # q.put('D')
    # q.put('A')
    edgesDict = dict()
    ##print "size of dictionary"+str(size(dict_Tree))
    # print "Visited Nodes Size()"
    # print len(visitedNodes)
    output = ''
    if (sourceNode == targetNode):
        remainingFuel = MaxFuel - fuelConsumed

        # print sourceNode+'-'+targetNode+' '+' '+remainingFuel
        output = sourceNode + '-' + targetNode + ' ' + ' ' + remainingFuel

    elif (sourceNode not in dict_Tree.keys()):
        # print'------- 1--------------'
        # print "No Path"
        output = "No Path"

    elif (targetNode not in dict_Tree.keys()):
        # print '------- 2--------'
        # print "No Path"
        output = "No Path"

    else:
        i = 0
        residualFuel = int(MaxFuel)
        # path.append(sourceNode)
        temp = 0
        output = ''
        # residualFuel=MaxFuel
        lastNodeVisited = ''
        lastEdgeWeight = 0
        finalNode = ''
        unableToReachTarget = False
        cummCost = 0
        output = ' '
        finalPath = ''
        totalCost = 0
        while len(q) != 0:
            # print "-----------------------"


            # print "Queue-->"+str(q)
            v, path, cummCost = q.pop()
            ##print "Vertex being expanded"+str(v)
            # print "path--->"+str(path)
            # print
            neighbours = dict()
            # print "&&&&&&&&&"+v
            if (v == targetNode and int(MaxFuel) >= int(cummCost)):
                # print "Path Found"+ path
                remainingFuel = int(MaxFuel) - int(cummCost)
                # print "remaining fuel-->"+str(remainingFuel)
                output = path + ' ' + str(remainingFuel)
                break

            if (v not in visitedNodes):

                edgesDict = dict_Tree.get(v)
                # print "neighbors--->"+str(edgesDict)
                visitedNodes.append(v)
                neighbors_vertices = edgesDict.keys()
                totalNeighbors = len(neighbors_vertices)
                # print "totalNeighbors---->"+str(totalNeighbors)
                # print "vertex being expanded now-->"+v
                # print sorted(edgesDict.keys())
                temp_queue = []
                # temp_queue.append(('B',10,15))
                # temp_queue.append(('A',20,30))
                # temp_queue.append(('C',50,12))
                # print "Sorted temp_queue-->"+str(sorted(temp_queue,reverse=False))
                targetNodeFound = False
                for key in sorted(edgesDict.keys()):
                    if key not in visitedNodes:
                        # print "inside if"

                        # fuelNeeded=int(MaxFuel)-(cummCost)
                        # weight=int(edgesDict[key])
                        totalFuel = cummCost + int(edgesDict[key])
                        # print "totalFuel-->"+str(totalFuel)+'MaxFuel'+str(MaxFuel)
                        if (int(MaxFuel) >= int(totalFuel)):
                            # print "node satified fuel condition"
                            if (key == targetNode):
                                finalPath = path + '-' + str(key)
                                totalCost = int(cummCost) + int(edgesDict[key])
                                remainingFuel = int(MaxFuel) - int(totalCost)

                            temp_queue.append((key, path + '-' + str(key), cummCost + int(edgesDict[key])))

            # print "sorted!!->"+str(temp_queue)
            for e1, e2, e3 in sorted(temp_queue, reverse=True):
                q.append((e1, e2, e3))

            # print"Queue after first traversal" +str(q)
            ##print "queue after pop"+str(len(q))

            # break
            if (targetNodeFound == True):
                # print "time to return to parent function"+ str(finalPath)+str(remainingFuel)
                break

        if (finalPath == ''):
            output = "No Path"
            # print "No path found!!!!!!!!!!!"

    return output


def UCS_Search(dict_Tree, sourceNode, targetNode, MaxFuel):
    # print "Inside UCS Search()"
    ##print "Inside BFS Search()"+sourceNode
    # print sourceNode+targetNode+MaxFuel
    # S=sourceNode
    S = sourceNode
    T = targetNode
    lastVisitedNode = ''
    fuelConsumed = 0
    # to check the nodes to be traversed
    # q = []
    # =Q.PriorityQueue()
    # q.append(sourceNode)


    lastNodeVisited = []

    # to keep track of the nodes already visited
    visitedNodes = []
    path = []
    # visitedNodes.append(sourceNode)
    # print "******"
    # print visitedNodes
    # sourceNode='D'
    ##print len(q)
    # q.put('D')
    # q.put('A')
    edgesDict = dict()
    ##print "size of dictionary"+str(size(dict_Tree))
    # print "Visited Nodes Size()"
    # print len(visitedNodes)

    # while not q.empty():
    ##print '++++'+q.get()

    # #print "Queue at the begining of the function call"
    # #print q.get()
    output = ''
    if (sourceNode == targetNode):
        remainingFuel = MaxFuel - fuelConsumed

        # print sourceNode+'-'+targetNode+' '+' '+remainingFuel
        output = sourceNode + '-' + targetNode + ' ' + ' ' + remainingFuel

    elif (sourceNode not in dict_Tree.keys()):
        # print'------- 1--------------'
        # print "No Path"
        output = "No Path"

    elif (targetNode not in dict_Tree.keys()):
        # print '------- 2--------'
        # print "No Path"
        output = "No Path"

    else:
        # print "hello else"
        visitedNodes = set()
        q = Z.PriorityQueue()
        residualFuel = MaxFuel

        q.put((int(0), sourceNode, sourceNode))
        goal = False

        while not q.empty() and not goal:
            cumCost, currentNode, path = q.get()
            # print "cumCost+currentNode+path"+str(cumCost)+currentNode+'********'+str(path)
            residualFuel = int(residualFuel) - cumCost
            # print "Residual fuel-->"+str(residualFuel)
            output = ''
            remainingFuel = 0
            if currentNode == targetNode and cumCost <= MaxFuel:
                remainingFuel = int(MaxFuel) - cumCost
                # print"goal reached"+path+str(remainingFuel)
                output = path + ' ' + str(remainingFuel)

                break
            elif currentNode == targetNode and cumCost > MaxFuel:

                # print"No Path"+path+str(residualFuel)
                output = "No Path"
                break

            else:
                if currentNode not in visitedNodes:
                    visitedNodes.add(currentNode)
                    edgesDict = dict_Tree.get(currentNode)

                    for key in edgesDict.keys():
                        if key not in visitedNodes:
                            # print "key being added"+key
                            # print "new cost"+str(cumCost+int(edgesDict[key]))
                            q.put((cumCost + int(edgesDict[key]), key, str(path) + '-' + str(key)))


                            # print "output--->"+output

    return output


    # parsing the input file


i = 0;
dict_edges = dict()
temp1 = dict()
for line in lines:
    ##print line
    if i == 0:
        algo = lines[0]
        # print 'algo: '+algo
        # algo="DFS"
        i = i + 1

    elif i == 1:
        target = lines[1]
        # print 'target: '+target
        i = i + 1
    elif i == 2:
        sourceNode = lines[2]
        # print 'sourceNode: '+sourceNode
        i = i + 1
    elif i == 3:
        targetNode = lines[3]
        # print 'targetNode: '+targetNode
        i = i + 1
    else:
        ##print line
        edges = line.split(':')
        ##print edges
        V1 = edges[0]
        ##print V1
        ##print edges[1]+'***'
        S2 = edges[1].split(',')
        # print S2
        temp = buildTree(V1, S2)
        dict_edges.update({V1: temp});

# print 'tree'
# print dict_edges
##print '***'+algo
if (algo == 'BFS'):
    output = BFS_Search(dict_edges, sourceNode, targetNode, target)
    fo = open("output.txt", "w")
    fo = open("output.txt", "w")
    # print "output return-->"+str(output)
    checkStr = str(output)
    fo.write(checkStr)
elif (algo == 'DFS'):
    output = DFS_Search(dict_edges, sourceNode, targetNode, target)
    fo = open("output.txt", "w")
    fo = open("output.txt", "w")
    # print "output return-->"+str(output)
    checkStr = str(output)
    fo.write(checkStr)
elif (algo == 'UCS'):
    output = UCS_Search(dict_edges, sourceNode, targetNode, target)
    fo = open("output.txt", "w")
    # print "output return-->"+str(output)
    checkStr = str(output)
    fo.write(checkStr)
    # fo.close

else:
    # print "Not a valid algorithm"


    fo.close()