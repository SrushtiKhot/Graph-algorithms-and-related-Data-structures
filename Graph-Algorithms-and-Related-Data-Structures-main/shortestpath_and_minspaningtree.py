# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 18:50:32 2021

@author: srevadig
"""
from datetime import datetime
import numpy as np
from collections import defaultdict
import heapq
from pprint import pprint

#Function to read input from input textfile
def input_textfile(textfile):
    temp = []
    with open(textfile, 'r') as fin:
        for line in fin:
            temp.append(line.split())
    return temp

#FUnction to extract information from the graph
def extract_graph(graph):
    start = 'dummy'
    v, u, type_of_graph = graph[0]
    v = int(v)
    u = int(u)
    l1=len(graph[-1])
    if (l1 == 1):
        start = graph[-1][0]
    rl=[v, u, type_of_graph, start]
    return(rl)

#Function to store information of the graph provided as paarmeter and store as adacency list
def store_ginfo(graph):
    v, u, type_of_graph, start = extract_graph(graph)

    adjacency_list = {}
    for i in range(1, u + 1):
        p, q, r = graph[i]
        k=adjacency_list.keys()
        if p not in k:
            adjacency_list[p] = {q: int(r)}
        else:
            adjacency_list[p].update({q: int(r)})
        k1=adjacency_list.keys()
        if q not in k1:
            adjacency_list[q] = {}

    # if the graph is undirected add the edges in the reverse order as well
    if type_of_graph == 'U':
        for i in range(1, u + 1):
            p, q, r, = graph[i]
            adjacency_list[q].update({p: int(r)})

    return adjacency_list, start

#Function to calculate shortest path using djikstra algorithm

def djistra_shortest_path_find(adjacency_list, start):
    shortest_path = {}

    # initialize all vertices distances and set the start to 0
    k1=adjacency_list.keys()
    for vert in k1:
        ni=np.inf
        shortest_path[vert] = {'distance':ni , 'parent': ''}
    shortest_path[start] = {'distance': 0, 'parent': '-'}

    # maintain a lookup for updating distances
    update_dist = {}
    # priority queue for shortest path to vertex
    shortest_path_pqueue = []

    # initialize heap with priority queue
    si=shortest_path.items()
    for vert, info in si:
        pqueue_start = [info['distance'], vert]
        update_dist[vert] = pqueue_start
        heapq.heappush(shortest_path_pqueue, pqueue_start)

    # run till the heap is not empty
    while len(shortest_path_pqueue) > 0:
        # get the minimum distance vertex
        h=heapq.heappop(shortest_path_pqueue)
        latest_dist, latest_vertex =h
        # update distances to all neighbors of the current minimum distance vertex
        for neighbouring_vertex, neighbouring_distance in adjacency_list[latest_vertex].items():
            distance = shortest_path[latest_vertex]['distance'] + neighbouring_distance
            # if distance of neighbors is lesser than current distance of neighbors, update distances
            # and add neighbor vertex to queue
            if distance < shortest_path[neighbouring_vertex]['distance']:
                shortest_path[neighbouring_vertex]['distance'] = distance
                shortest_path[neighbouring_vertex]['parent'] = latest_vertex
                update_dist[neighbouring_vertex][0] = distance
                heapq.heappush(shortest_path_pqueue, [distance, neighbouring_vertex])

    return shortest_path

#Calculate minimun spanning tree according to prim's algorithm
def minimum_spanning_tree_prim(adjacency_list, start):
    minimum_spanning_tree = defaultdict(set)

    # initialize all edges in the graph
    visited_edges = set([start])
    aitems= adjacency_list[start].items()
    edges = [(cost, start, terminate) for terminate, cost in aitems]
    # heapify edges to get the shortest edge distances
    heapq.heapify(edges)

    # run till all edges are traversed
    while edges:
        print(edges)
        # get minimum weight edge
        cost, parent, terminate = heapq.heappop(edges)
        # if the other end vertex is has not been visited yet, visit it
        if terminate not in visited_edges:
            visited_edges.add(terminate)
            # update MST to include the minimum weight edge
            ct=(cost, terminate)
            minimum_spanning_tree[parent].add(ct)
            # heapify the neighbors of the recently visited neighbor node
            ai1=adjacency_list[terminate].items()
            for to_next, cost in ai1:
                # if the other end vertex is has not been visited yet, add neighbours to heap
                if to_next not in visited_edges:
                    tup=(cost, terminate, to_next)
                    heapq.heappush(edges,tup )

    return minimum_spanning_tree

def user_choice(selected_option):
    
    user_options_graphs = {	
                '1': 'undirected_1.txt',
                '2': 'undirected_2.txt',
                '3': 'undirected_3.txt',
                '4': 'directed_1.txt',
                '5': 'directed_2.txt',
                '6': 'directed_3.txt'}
    len_option=len(selected_option)
    if  len_option== 1:
        graph_considered = input_textfile(user_options_graphs[selected_option])
    else:
        graph_considered = input_textfile(selected_option)
    return graph_considered, user_options_graphs[selected_option]

selected_option = input("PLEASE SELECT A NUMBER 1 TO 6 TO SELECT THE GRAPH.ENTER FILE NAME IF YOU WANT TO TEST OTHER FILES\n")
graph_considered, chosen_graph = user_choice(selected_option)
print("\nTHE SELECTED GRAPH IS: ", chosen_graph)
adjacency_list, start = store_ginfo(graph_considered)

print("\nREPRESENTATION OF ADJACENCY LIST OF GRAPH:")
pprint(adjacency_list)

if (start == 'dummy'):
    print("SOURCE NODE NOT PROVIDED.")
    key=adjacency_list.keys()
    start = list(key)[0]

print("\nSOURCE: ", start)
print()

start_time_1= datetime.now()


x = djistra_shortest_path_find(adjacency_list, start)
print('SHORTEST PATH USING DJISTRA:')
for key in sorted(x):
    print(key, ':', x[key])
print()
end_time_1 = datetime.now()
print('Duration: {}'.format(end_time_1 - start_time_1))
start_time_2= datetime.now()
y = minimum_spanning_tree_prim(adjacency_list, start)
total_cost = 0
print('MINIMUM SPANNING TREE:')
for key in sorted(y):
    print(key, ':', y[key])
    for element in y[key]:
        total_cost += element[0]
print('COST: ', total_cost)
end_time_2 = datetime.now()
print('Duration: {}'.format(end_time_2 - start_time_2))


