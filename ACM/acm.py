#Nom, Matricule
#Nom, Matricule

import math
import numpy as np
import sys
import heapq
INFINITY = math.inf

def calculate_all_distances(points):
    # Vectorized distance calculation
    diff = points[:, np.newaxis, :] - points[np.newaxis, :, :]
    dist_matrix = np.sqrt(np.sum(diff**2, axis=-1))
    return dist_matrix

def prim(problems):
    n_nodes = len(problems)  # Use 'problems' instead of 'points'
    if n_nodes == 0: 
        return 0  # Handle empty graph case
    
    # Initialize with infinite weights and set the first node's weight to 0 to start from it
    min_edge = np.full(n_nodes, np.inf)
    min_edge[0] = 0
    
    visited = np.zeros(n_nodes, dtype=bool)
    mst_weight = 0
    
    for _ in range(n_nodes):
        # Select the unvisited node with the smallest distance to the MST
        u = np.argmin(min_edge)
        mst_weight += min_edge[u]
        visited[u] = True
        min_edge[u] = np.inf  # Ensure this node is not selected again
        
        # For unvisited nodes, calculate distances from the newly added node and update if smaller
        if n_nodes - np.sum(visited) > 0:  # Check if there are unvisited nodes left
            # Correct the call to calculate_all_distances for the current context
            dist_to_u = calculate_all_distances(problems[[u], :])[0, ~visited]
            min_edge[~visited] = np.minimum(min_edge[~visited], dist_to_u)
    
    return mst_weight
#Fonctions pour lire/écrire dans les fichier. Vous pouvez les modifier, 
#faire du parsing, rajouter une valeur de retour, mais n'utilisez pas
#d'autres librairies.
#Functions to read/write in files. you can modify them, do some parsing,
#add a return value, but don't use other librairies
def read_problems(input_file):
    with open(input_file, 'r') as file:
        lines = file.read().splitlines()

    problems = []
    line_index = 1  # Skip the first line which is not part of the problems

    while line_index < len(lines):
        n_nodes = int(lines[line_index])
        line_index += 1
        problem_data = lines[line_index:line_index + n_nodes]
        problem = np.array([list(map(float, line.split())) for line in problem_data])
        problems.append(problem)
        line_index += n_nodes

    return problems

def write(fileName, content):
    with open(fileName, "w") as file:
        file.write(content)

def main(args):
    input_file = args[0]
    output_file = args[1]

    problems = read_problems(input_file)
    results = []

    for problem in problems:
        mst_weight = prim(problem)
        results.append(f"{mst_weight}")

    write(output_file, "\n".join(results))

#NE PAS TOUCHER
#DO NOT TOUCH
if __name__ == '__main__':
    main(sys.argv[1:])
    