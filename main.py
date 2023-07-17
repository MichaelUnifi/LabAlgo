import Graph
import DisjointList as dl
import DisjointForest as df
import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

n_nodes_1 = 5050
n_repeats = 30
step_1 = 50
n_nodes_2 = 15100
step_2 = 100


def no_weight_list_test(n_nodes, step):
    times = []
    for n in range(step, n_nodes, step):
        graph = Graph.Graph()
        listSet = dl.ListSet()
        for i in range(0, n_nodes):
            node = dl.Node(i)
            graph.addNode(node)
            listSet.makeSet(node)
        nodes = graph.getNodes()
        for i in range(0, n):
            rand = random.randint(0, n - 1)
            graph.addEdge([nodes[i], nodes[(i + rand) % n]])
        edges = graph.getEdges()
        timer_start = timer()
        for edge in edges:
            if listSet.findSet(edge[0]) != listSet.findSet(edge[1]):
                listSet.union(edge[0], edge[1])
        timer_end = timer()
        times.append((timer_end - timer_start)*1000)
    return times

def weight_list_test(n_nodes, step):
    times = []
    for n in range(step, n_nodes, step):
        graph = Graph.Graph()
        listSet = dl.ListSet()
        for i in range(0, n_nodes):
            node = dl.Node(i)
            graph.addNode(node)
            listSet.makeSet(node)
        nodes = graph.getNodes()
        for i in range(0, n):
            rand = random.randint(0, n - 1)
            graph.addEdge([nodes[i], nodes[(i + rand) % n]])
        edges = graph.getEdges()
        timer_start = timer()
        for edge in edges:
            if listSet.findSet(edge[0]) != listSet.findSet(edge[1]):
                listSet.weightedUnion(edge[0], edge[1])
        timer_end = timer()
        times.append((timer_end - timer_start)*1000)
    return times

def forest_test(n_nodes, step):
    times = []
    for n in range(step, n_nodes, step):
        graph = Graph.Graph()
        forest = df.Forest()
        for i in range(0, n_nodes):
            node = df.Node(i)
            graph.addNode(node)
            forest.makeSet(node)
        nodes = graph.getNodes()
        for i in range(0, n):
            rand = random.randint(0, n - 1)
            graph.addEdge([nodes[i], nodes[(i + rand) % n]])
        edges = graph.getEdges()
        timer_start = timer()
        for edge in edges:
            if forest.findSet(edge[0]) != forest.findSet(edge[1]):
                forest.union(edge[0], edge[1])
        timer_end = timer()
        times.append((timer_end - timer_start)*1000)
    return times

def empty_directory(directory):
    for file in os.listdir(directory):
        path=os.path.join(directory, file)
        os.remove(path)

def main():
    # Test 1
    x_axis = range(step_1, n_nodes_1, step_1)
    nw_times = np.zeros(len(x_axis))
    w_times = np.zeros(len(x_axis))
    f_times = np.zeros(len(x_axis))
    for i in range(0, n_repeats):
        nw_times += no_weight_list_test(n_nodes_1, step_1)
        w_times += weight_list_test(n_nodes_1, step_1)
        f_times += forest_test(n_nodes_1, step_1)
    nw_times /= n_repeats
    w_times /= n_repeats
    f_times /= n_repeats

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
    data = {'Number of Nodes': x_axis, 'Not Weighted List': nw_times, 'Weighted List': w_times, 'Disjoint Forest': f_times}
    df = pd.DataFrame(data)
    df1 = df.iloc[:40, :]
    df2 = df.iloc[40:70, :]
    df3 = df.iloc[70:, :]

    plt.clf()
    plt.figure(figsize=(10, 10))
    plt.title("Table of results")
    plt.axis('off')
    table = plt.table(cellText=df1.values, colLabels=df1.columns, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    plt.savefig('tables/table_1.png')
    plt.show()

    plt.clf()
    plt.figure(figsize=(10, 7))
    plt.axis('off')
    table = plt.table(cellText=df2.values, colLabels=df2.columns, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    plt.savefig('tables/table_2.png')
    plt.show()
    plt.clf()


    plt.figure(figsize=(10, 7))
    plt.axis('off')
    table = plt.table(cellText=df3.values, colLabels=df3.columns, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    plt.savefig('tables/table_3.png')
    plt.show()

    # Test 2
    x_axis = range(step_2, n_nodes_2, step_2)
    w_times = np.zeros(len(x_axis))
    f_times = np.zeros(len(x_axis))
    for i in range(0, n_repeats):
        w_times += weight_list_test(n_nodes_2, step_2)
        f_times += forest_test(n_nodes_2, step_2)
    w_times /= n_repeats
    f_times /= n_repeats
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
