
#################### CS 216: Design and Analysis of Algorithms Project ##################################
#################### Optimization of Telecommunication Network Design ###########################
                   #####   Madhawee Alabdulkreem - Shahad Baelayan	 ######

################ Brute-force algorithm ####################
import itertools 

#The user will enter the number of vertices
VerticesNum = int(input("Please Enter the number of cell towers: "))
Weights=[]
print("Enter the costs of installing connections between each pair of vertices: ")
print()
for i in range(VerticesNum):                
    row = list(map(int, input().split()))   
    Weights.append(row)

#This function will return the min cost and it's subset 
def BurutForce(Weights):  
    optimalSubset = None
    minCost = float('inf')                 
    VerticesNum = len(Weights) 
    towers = list(range(VerticesNum))
    permutations = itertools.permutations(towers) 

    print("All possible Subsets and Their Costs: ")
    for subset in permutations:
        if isCovered(subset, VerticesNum):             
            totalCostValue = calcCost(subset, Weights)  
            print("Subset: ", subset, " it's Cost: ", totalCostValue)
            if totalCostValue < minCost:
                minCost = totalCostValue
                optimalSubset = subset

    return  optimalSubset,minCost

#This function will return true if the subset covers all areas
def isCovered(subset, VerticesNum):                 
    return set(subset) == set(range(VerticesNum))

#This function will return totalCost 
def calcCost (subset, Weights):                      
    totalCostValue = 0  
    for i in range(len(subset)- 1):
        totalCostValue += Weights[subset[i]][subset[i + 1]]
    return totalCostValue


optimalSubset, minCost = BurutForce(Weights)
print("The Optimal Subset is:", optimalSubset, " And the Minimum Cost of the Optimal Subset is " , minCost)



############################################################################################################################

################ Greedy Algorithm -Kruskal- ###################

#This function will create a graph based on the input data from the user 
def graphMaker():
    verticesNum = int(input("Please Enter the number of cell towers: "))
    graph=[]
    print("Enter the costs of installing connections between each pair of vertices: ")
    for i in range(verticesNum):
        row = list(map(int, input().split()))
        graph.append(row)
    return graph

#This function will return MST & MSTC using kruskal 
def KruskalMST(graph):
    verticesNum = len(graph)

#This function will Sort edges in ascending order 
    def sortEdges(graph):
        edges = []
        for i in range(verticesNum):
            for j in range(i + 1, verticesNum):
                if graph[i][j] != 0:
                    edge = [i, j, graph[i][j]]
                    edges.append(edge)
        edges.sort(key=lambda x: x[2])
        return edges
    
    #for the disjointset 
    def initializeDisjointSet(vertices):
        disjointSet = []
        for c in range(vertices):
            disjointSet.append([c])
        return disjointSet
    
    #This function will check if the edge will form a circle 
    def formCycle(disjointSet, edge):
        i, j, _ = edge
        for c in disjointSet:
            if i in c and j in c:
                return True
        return False
    
    #This function will merges the sets 
    def mergeSets(disjointset, edge):
        i, j, _ = edge
        for c in disjointset:
            if i in c:
                seti = c
            if j in c:
                setj = c
        seti.extend(setj)
        disjointSet.remove(setj)

    edges = sortEdges(graph)
    MST = []
    totalWeight = 0
    disjointSet = initializeDisjointSet(verticesNum)

    while len(MST) < verticesNum - 1:
        edge = edges.pop(0)
        if not formCycle(disjointSet, edge):
            MST.append(edge)
            mergeSets(disjointSet, edge)
            totalWeight += edge[2]

    return MST, totalWeight

graph = graphMaker()
MST = KruskalMST(graph)
print("The Optimal Subset is:", MST[0]," And the Minimum Cost of the Optimal Subset is ", MST[1] )

