x =[]
with open("adj_matrix.txt") as f:
        while True:
                c = f.read(4)
                x.append(c.rstrip())
                if not c:
                        break
        x.remove('')
matrix = [] # a matrix of all elements from the text file in a list
for item in x:
        matrix.append(float(item))
length_matrix = len(matrix)
number_of_nodes = int(len(matrix)**0.5)
new_matrix =[] # a 2d matrix with distances as elements and nodes as indexes
for i in range(0, len(matrix), number_of_nodes):
        new_matrix.append(matrix[i:i+number_of_nodes])
print(new_matrix)
almost_graph = {}
graph = {}
for j in new_matrix[0]:
        almost_graph[new_matrix[0].index(j)] = j
graph[0] = almost_graph
for j in new_matrix[1]:
        almost_graph[new_matrix[1].index(j)] = j
graph[1] = almost_graph
for j in new_matrix[2]:
        almost_graph[new_matrix[2].index(j)] = j
graph[2] = almost_graph
for j in new_matrix[3]:
        almost_graph[new_matrix[3].index(j)] = j
graph[3] = almost_graph
print(graph)
