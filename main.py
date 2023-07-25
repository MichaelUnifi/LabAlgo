import Graph
import DisjointList as dl
import DisjointForest as df
import random
import timeit
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

n_nodes_1 = 3050
n_repeats = 30
step_1 = 50
n_nodes_2 = 15100
step_2 = 100

def measure_time(function, n_repeats):
    return timeit.timeit(stmt=lambda: function(), number=n_repeats)*1000/n_repeats

def test_first(n_nodes, step):
    n_list_times= []
    w_list_times = []
    forest_times = []
    components = []
    components_number = []
    for i in range(step, n_nodes, step):
        graph = Graph.Graph()
        for j in range(0, i):
            graph.addNode(Graph.Node(j))
        nodes = graph.getNodes()
        for j in range(len(nodes)):
            rand = random.randint(1, len(nodes)-1)
            graph.addEdge((nodes[j], nodes[(j+rand)%len(nodes)]))
        n_list_times.append(measure_time(lambda: graph.find_connected_components_list_unweighted(), n_repeats))
        w_list_times.append(measure_time(lambda: graph.find_connected_components_list_weighted(), n_repeats))
        forest_times.append(measure_time(lambda: graph.find_connected_components_forest(), n_repeats))
        components.append(graph.getComponents())
        components_number.append(graph.getComponentsNumber())
    return n_list_times, w_list_times, forest_times, components, components_number

def test_second(n_nodes, step):
    w_list_times = []
    forest_times = []
    for i in range(step, n_nodes, step):
        graph = Graph.Graph()
        for j in range(0, i):
            graph.addNode(Graph.Node(j))
        nodes = graph.getNodes()
        for j in range(len(nodes)):
            rand = random.randint(1, len(nodes) - 1)
            graph.addEdge((nodes[j], nodes[(j + rand) % len(nodes)]))
        w_list_times.append(measure_time(lambda: graph.find_connected_components_list_weighted(), n_repeats))
        forest_times.append(measure_time(lambda: graph.find_connected_components_forest(), n_repeats))
    return w_list_times, forest_times

def empty_directory(directory):
    for file in os.listdir(directory):
        path=os.path.join(directory, file)
        os.remove(path)

def main():
    # Test 1
    x_axis = range(step_1, n_nodes_1, step_1)
    nw_times, w_times, f_times, components, components_number = test_first(n_nodes_1, step_1)

    nw_times= [round(x, 4) for x in nw_times]
    w_times = [round(x, 4) for x in w_times]
    f_times = [round(x, 4) for x in f_times]

    empty_directory("imgs")

    empty_directory("tables")
    #plot test 1
    plt.clf()
    plt.plot(x_axis, nw_times, color="blue", label="Not Weighted List")
    plt.plot(x_axis, w_times, color="red", label="Weighted List")
    plt.plot(x_axis, f_times, color="green", label="Disjoint Forest")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Time (ms)")
    plt.title("Connected components find comparison")
    plt.legend()
    plt.savefig("imgs/union_comparison.png")
    plt.show()
    #create table, split in 3 parts
    data = {'Number of Nodes': x_axis, 'Not Weighted List': nw_times, 'Weighted List': w_times, 'Disjoint Forest': f_times, 'Components': components, 'Components Number': components_number}

    df = pd.DataFrame(data)
    plt.clf()
    plt.figure(figsize=(15, 15))
    plt.axis('off')
    table = plt.table(cellText=df.values, colLabels=df.columns, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    plt.savefig('tables/table.png')
    plt.show()

    # Test 2
    x_axis = range(step_2, n_nodes_2, step_2)
    w_times, f_times = test_second(n_nodes_2, step_2)
    # plot test 2
    plt.clf()
    plt.plot(x_axis, w_times, color="red", label="Weighted List")
    plt.plot(x_axis, f_times, color="green", label="Disjoint Forest")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Time (ms)")
    plt.title("Improved Data Structures Comparison")
    plt.legend()
    plt.savefig("imgs/improved_comparison.png")
    plt.show()




if __name__ == '__main__':
    main()
