#Canelle Wagner, 20232321
#Alex Maggioni, Matricule

import math
import numpy as np
import sys
import time
INFINITY = math.inf

def read_problems(input_file):
    problems = []  
    with open(input_file, 'r') as file:
        total_problems = int(file.readline().strip())  
        for _ in range(total_problems):
            num_nodes = int(file.readline().strip())  
            nodes = []  
            for _ in range(num_nodes):
                line = file.readline().strip()
                x, y = map(float, line.split())  
                nodes.append((x, y))  
            problems.append(nodes)
    return problems

def write(fileName, content):
    with open(fileName, "w") as file:
        file.write(content)

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def build_adjacency_matrix(nodes):
    points = np.array(nodes)
    num_nodes = len(nodes)
    x = points[:, None, :] - points[None, :, :]
    dist_matrix = np.sqrt(np.sum(x ** 2, axis=2))
    np.fill_diagonal(dist_matrix, 0)
    dist_matrix[dist_matrix == 0] = INFINITY
    return dist_matrix

def prim_algorithm(L):
    n = len(L)
    in_mst = np.zeros(n, dtype=bool)
    mindist = np.full(n, INFINITY)
    mindist[0] = 0
    total_weight = 0
    for _ in range(n):
        u = np.argmin(np.where(in_mst, INFINITY, mindist))
        in_mst[u] = True
        total_weight += mindist[u]
        for v in range(n):
            if L[u, v] < mindist[v] and not in_mst[v]:
                mindist[v] = L[u, v]
    return total_weight

def main(args):
    input_file = args[0]
    output_file = args[1]
    problems = read_problems(input_file)
    mst_weights = []
    for nodes in problems:
        start_time = time.time()
        adjacency_matrix = build_adjacency_matrix(nodes)
        mst_weight = prim_algorithm(adjacency_matrix)
        mst_weights.append(f"{mst_weight}")
        end_time = time.time()  # End timing
        elapsed_time = end_time - start_time
        print(f"Computed MST weight for {len(nodes)} nodes in {elapsed_time:.4f} seconds.")
    write(output_file, "\n".join(mst_weights))

if __name__ == '__main__':
    main(sys.argv[1:])