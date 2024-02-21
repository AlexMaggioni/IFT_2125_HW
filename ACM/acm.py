#Alex Maggioni, 20266243
#Canelle Wagner, 20232321

import math
import sys
import time

def read_problems(input_file):
    problems = []  
    with open(input_file, 'r') as file:
        total_problems = int(file.readline().strip())  
        for _ in range(total_problems):
            num_nodes = int(file.readline().strip())  
            nodes = []  
            for _ in range(num_nodes):
                x, y = map(float, file.readline().strip().split())  
                nodes.append((x, y))  
            problems.append(nodes)
    return problems

def write(fileName, content):
    with open(fileName, "w") as file:
        file.write(content)

def build_adjacency_matrix(nodes):
    num_nodes = len(nodes)
    dist_matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            dist = math.sqrt((nodes[i][0] - nodes[j][0]) ** 2 + (nodes[i][1] - nodes[j][1]) ** 2)
            dist_matrix[i][j] = dist_matrix[j][i] = dist
    return dist_matrix

def prim_algorithm(L):
    n = len(L)
    in_mst = [False] * n
    mindist = [float('inf')] * n
    mindist[0] = 0
    total_weight = 0
    for _ in range(n):
        min_value = float('inf')
        u = -1
        for i in range(n):
            if not in_mst[i] and mindist[i] < min_value:
                min_value = mindist[i]
                u = i
        in_mst[u] = True
        total_weight += mindist[u]
        for v in range(n):
            if L[u][v] > 0 and not in_mst[v] and L[u][v] < mindist[v]:
                mindist[v] = L[u][v]
    return total_weight

def main(args):
    input_file = args[0]
    output_file = args[1]
    problems = read_problems(input_file)
    mst_weights = []
    for nodes in problems:
        adjacency_matrix = build_adjacency_matrix(nodes)
        mst_weight = prim_algorithm(adjacency_matrix)
        mst_weights.append(str(mst_weight))
    write(output_file, "\n".join(mst_weights))

if __name__ == '__main__':
    main(sys.argv[1:])