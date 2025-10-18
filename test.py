import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations
import sys

def main():
    directed = True # 有向グラフの場合はTrue、無向グラフの場合はFalse
    plot = True     # グラフをプロットする場合はTrue、しない場合はFalse
    input = []      # 入力データを格納するリスト

    # 標準入力の読み込み
    for line in sys.stdin:
        cleaned_line = line.strip()
        if not cleaned_line:
            continue
        parts = cleaned_line.split(',')
        print(parts)
        input.append(parts)

    # 最長経路の計算
    calculate_longest_path(input, directed, plot)

# 入力されたグラフの情報から最長経路を例さんする関数
def calculate_longest_path(input: list, directed: bool, plot: bool):
    # グラフオブジェクトの作成
    if directed:
        G = nx.DiGraph()    # 有向グラフオブジェクトを作成
    else:
        G = nx.Graph()      # 無向グラフオブジェクトを作成

    for row in input:
        u, v, w = int(row[0]), int(row[1]), float(row[2])
        G.add_edge(u, v, weight=w)

    # ノードのリストを取得
    nodes = list(G.nodes())

    # 始点と終点が異なる場合の最長経路を探索
    max_length = -1
    best_path = None
    for start, end in combinations(nodes, 2):
        try:
            for path in nx.all_simple_paths(G, source=start, target=end):
                length = nx.path_weight(G, path, weight='weight')
                if length > max_length:
                    max_length = length
                    best_path = path
        except nx.NetworkXNoPath:
            continue
    
    # 始点と終点が同じ場合の最長経路を探索
    max_cycle_length = -1
    best_cycle = None
    for cycle in nx.simple_cycles(G):
        path = cycle + [cycle[0]]  # サイクルを閉じる
        length = nx.path_weight(G, path, weight='weight')

        if length > max_cycle_length:
            max_cycle_length = length
            best_cycle = path

    # 最長経路を出力
    if max_length > max_cycle_length:
        print("最長経路長:{}".format(max_length))
        for node in best_path:
            print(node, end='\r\n')
    elif max_cycle_length > -1:
        print("最長経路長:{}".format(max_cycle_length))
        for node in best_cycle:
            print(node, end='\r\n')

    # グラフの可視化
    if plot:
        pos = nx.spring_layout(G, seed=42)
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, font_weight='bold')
        weights = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
        plt.show()

if __name__ == "__main__":
    main()