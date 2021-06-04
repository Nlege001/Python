#Name: Naol Legesse
#Name of project: Dijkstra's Algorithim
#Collaborator: Elizabeth Ashley
#Goal: to find the shortest distance between two nodes of a graph using the concepts of BFS and merge sort
#Date: 11/24/2020

#*********************************** Start of algorithim ***************************************************************

x =[] # creating a list to store read items from the given adjecency matrix
with open("adj_matrix.txt") as f:  #opening the text file(any text file representing an adjecency matrix)
        while True:
                c = f.read(4)
                x.append(c.rstrip())
                if not c:
                        break
        x.remove('')
matrix = [] # a of all elements from the text file in a list with an integer data type
for item in x:
        matrix.append(float(item))
length_matrix = len(matrix)
number_of_nodes = int(len(matrix)**0.5) #this represents the total number of nodes in the graph 
new_matrix =[] #a 2d matrix with distances as elements and nodes as indexes
for i in range(0, len(matrix), number_of_nodes):
        new_matrix.append(matrix[i:i+number_of_nodes]) #this creates a 2d list new_matrix 
almost_graph = {} # a linked list(dictionary) of distances of nodes from other nodes
graph = {} # final graph in the form of {'a': {'b': 10, 'c': 3}, 'b': {'c': 1, 'd': 2}, 'c': {'b': 4, 'd': 8, 'e': 2}, 'd': {'e': 7}, 'e': {'d': 9}}
for i in range(number_of_nodes):
    for j in new_matrix[i]:
        if j != 0.0:
            almost_graph[new_matrix[i].index(j)] = j
    graph[i]= almost_graph
print(graph)
 #***************************************** End of parsing and Dijkstra's algorithm below ************************************

def dijkstra(graph, start, goal): # takes the graph, a start node and an end node fpr the algorithim
    shortest_distance = {} 
    predecessor = {}  # preceding node
    unseenNodes = graph 
    infinity = 9999999 # a virtal number representing infinity 
    path = [] 
    for node in unseenNodes:
        shortest_distance[node] = infinity # set shortest distance to infinity
    shortest_distance[start] = 0

    while unseenNodes: #iterate thourgh unseen nodes until we find the shortest distance 
        minNode = None 
        for node in unseenNodes:
            if minNode is None:     #condtion to proceed to next node 
                minNode = node  #set newly seen node to minmode for later comparison
            elif shortest_distance[node] < shortest_distance[minNode]: # compare the distances form the start node to the newly visted node
                minNode = node # if distance is less than previous node, set minnode to newnode

        for childNode, weight in graph[minNode].items(): #loop to iterate thourgh graph
            if weight + shortest_distance[minNode] < shortest_distance[childNode]: # compare the distances of the parent node(minnode) wit its child nodes
                shortest_distance[childNode] = weight + shortest_distance[minNode] #update shortest distance 
                predecessor[childNode] = minNode # set the node to predecessor
        unseenNodes.pop(minNode) # remove minnode form path as minnode has been visted and checked

    currentNode = goal # set our current node to our goal i.e our final destination
    while currentNode != start: # condtion will make sure that we dont try to find the shortest distance from a node to itself
        try:
            path.insert(0, currentNode) #insert seen nodes to the path list
            currentNode = predecessor[currentNode] 
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0, start)
    if shortest_distance[goal] != infinity: 
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('And the path is ' + str(path))


dijkstra(graph, 1, 3)
#dijkstra(graph, 2, 3) ----there is no path between the nodes and hence the algorithm will show a path not reachable output



#****************************************** END OF ALGORITHM ******************************************************