import networkx as nx
import matplotlib.pyplot as plt
import yaml

def visualize_pipeline(config_path):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    G = nx.DiGraph()
    prev = None
    for step in config['pipeline']:
        G.add_node(step["name"], label=step["type"])
        if prev:
            G.add_edge(prev, step["name"])
        prev = step["name"]

    pos = nx.spring_layout(G)
    labels = nx.get_node_attributes(G, 'label')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10)
    nx.draw_networkx_labels(G, pos, labels)
    plt.show()

# Example
# visualize_pipeline("config/sample_pipeline.yaml")
