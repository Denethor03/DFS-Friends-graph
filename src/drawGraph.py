import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


COLOUR_REGULAR   = "#4A90D9"
COLOUR_FAVOURITE = "#E8525A"
COLOUR_EDGE      = "#AAAAAA"
COLOUR_BG        = "#1E1E2E"
COLOUR_LABEL     = "#FFFFFF"


def buildGraph(node, graph, colorMap):
    colorMap[node.name] = COLOUR_FAVOURITE if node.isFavouriteFriend else COLOUR_REGULAR
    for child in node.children:
        graph.add_edge(node.name, child.name)
        buildGraph(child, graph, colorMap)


def hierarchicalPos(G, root, width=1.0, vertGap=0.3, vertLoc=0,
                    xCenter=0.5, pos=None, parent=None):
    if pos is None:
        pos = {root: (xCenter, vertLoc)}
    else:
        pos[root] = (xCenter, vertLoc)

    children = [n for n in G.neighbors(root) if n != parent]

    if children:
        dx = width / len(children)
        nextX = xCenter - width / 2 + dx / 2
        for child in children:
            pos = hierarchicalPos(G, child, width=dx, vertGap=vertGap,
                                  vertLoc=vertLoc - vertGap, xCenter=nextX,
                                  pos=pos, parent=root)
            nextX += dx
    return pos


def drawTree(root):
    graph = nx.DiGraph()
    colorMap = {}

    graph.add_node(root.name)
    buildGraph(root, graph, colorMap)

    pos = hierarchicalPos(graph, root.name)
    colors = [colorMap[node] for node in graph.nodes()]

    fig, ax = plt.subplots(figsize=(14, 8))
    fig.patch.set_facecolor(COLOUR_BG)
    ax.set_facecolor(COLOUR_BG)

    nx.draw_networkx_edges(
        graph, pos, ax=ax,
        edge_color=COLOUR_EDGE,
        arrows=True,
        arrowstyle="-|>",
        arrowsize=20,
        width=1.5,
        connectionstyle="arc3,rad=0.05"
    )

    nx.draw_networkx_nodes(
        graph, pos, ax=ax,
        node_color=colors,
        node_size=2200,
        linewidths=2,
        edgecolors="#FFFFFF"
    )

    nx.draw_networkx_labels(
        graph, pos, ax=ax,
        font_color=COLOUR_LABEL,
        font_size=9,
        font_weight="bold"
    )

    legend = [
        mpatches.Patch(color=COLOUR_FAVOURITE, label="Favourite friend"),
        mpatches.Patch(color=COLOUR_REGULAR,   label="Regular"),
    ]
    ax.legend(
        handles=legend,
        loc="upper right",
        facecolor="#2E2E3E",
        edgecolor="#555555",
        labelcolor=COLOUR_LABEL,
        fontsize=10
    )

    ax.set_title("Friend Tree", color=COLOUR_LABEL, fontsize=14, fontweight="bold", pad=15)
    ax.axis("off")
    plt.tight_layout()
    plt.show()