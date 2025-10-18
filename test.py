import pandas as pd
from graphillion import GraphSet as gs
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from itertools import combinations

def get_longest_path(weights, stations):
    # 始点と終点が異なる場合の最長経路を探索
    adj_matrix = np.zeros((len(stations), len(stations))) # 隣接行列の初期化 start x end
    for start,end in combinations(stations,2):
        paths = gs.paths(start,end)
        if not paths:
            continue
        max_path = next(paths.max_iter(weights))
        distance = 0
        for edge in max_path:
            distance += weights[edge]
        adj_matrix[stations.index(start)][stations.index(end)] = distance
    
    # 始点と終点が同じ場合の最長経路を探索
    cycles = gs.cycles()
    if cycles:
        for cycle in cycles:
            print("cycle:", cycle)


        
        


    # paths = gs.paths(1,4)
    # max_path = next(paths.max_iter(weights))
    # distance = 0
    # for edge in max_path:
    #     distance += weights[edge]
    # print(distance)

# 入力されたグラフの情報から最長経路を例さんする関数
def calculate_longest_path():
    df_list = pd.read_csv('test.csv', sep=',', header=None)
    univ =[]
    weights = {}
    stations = []

    for index,row in df_list.iterrows():
        edge = (int(row.iloc[0]), int(row.iloc[1]))
        univ.append(edge)
        weights[edge] = float(row.iloc[2])
        if int(row.iloc[0]) not in stations:
            stations.append(int(row.iloc[0]))
        if int(row.iloc[1]) not in stations:
            stations.append(int(row.iloc[1]))

    stations.sort()
    print("Stations:", stations)
    print("univ:", univ)
    gs.set_universe(univ)
    get_longest_path(weights, stations)

    paths = gs.paths(1,4)
    max_path = next(paths.max_iter(weights))
    distance = 0
    for edge in max_path:
        distance += weights[edge]
    print(distance)

    G = nx.DiGraph()
    G.add_edges_from(gs.universe())
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
    plt.show()

def main():
    calculate_longest_path()

if __name__ == "__main__":
    main()