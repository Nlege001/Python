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
print(matrix)
length_matrix = len(matrix)
number_of_nodes = int(len(matrix)**0.5)
print(number_of_nodes)
new_matrix =[] # a 2d matrix with distances as elements and nodes as indexes
for i in range(0, len(matrix), number_of_nodes):
        new_matrix.append(matrix[i:i+number_of_nodes])
print(new_matrix)
almost_graph = {}
graph = {}
for i in range(number_of_nodes):
    print(i)
    for j in new_matrix[i]:
        print(j)
        almost_graph[new_matrix[i].index(j)] = j
    graph[i]= almost_graph
print(graph)