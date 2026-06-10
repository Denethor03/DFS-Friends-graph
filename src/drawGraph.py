import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.table import Table

COLOUR_REGULAR   = "#4A90D9"
COLOUR_FAVOURITE = "#E8525A"
COLOUR_EDGE      = "#AAAAAA"
COLOUR_BG        = "#1E1E2E"
COLOUR_LABEL     = "#FFFFFF"
COLOUR_OK        = "#00FF00"      # green border – no conflict
COLOUR_CONFLICT  = "#FF0000"      # red border – conflict

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

def drawTree(root, conflict_results):
    graph = nx.DiGraph()
    colorMap = {}

    graph.add_node(root.name)
    buildGraph(root, graph, colorMap)

    pos = hierarchicalPos(graph, root.name)
    
    node_edgecolors = {}
    for node in graph.nodes():
        if node in conflict_results:
            if conflict_results[node]: 
                node_edgecolors[node] = COLOUR_CONFLICT
            else:
                node_edgecolors[node] = COLOUR_OK
        else:
            node_edgecolors[node] = "#FFFFFF"

    fig, ax = plt.subplots(figsize=(16, 9))
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

    for node in graph.nodes():
        nx.draw_networkx_nodes(
            graph, pos, ax=ax,
            nodelist=[node],
            node_color=[colorMap[node]],
            node_size=2200,
            linewidths=3,
            edgecolors=[node_edgecolors[node]]
        )

    nx.draw_networkx_labels(
        graph, pos, ax=ax,
        font_color=COLOUR_LABEL,
        font_size=9,
        font_weight="bold"
    )

    left, width = 0.05, 0.65
    bottom, height = 0.1, 0.8
    ax.set_position([left, bottom, width, height])
    
    table_ax = fig.add_axes([left + width + 0.02, bottom, 0.25, height])
    table_ax.axis('off')
    table_ax.set_facecolor(COLOUR_BG)
    
    fav_nodes = sorted(conflict_results.keys())
    table_data = []
    for node in fav_nodes:
        others = conflict_results[node]
        status = f"CONFLICT: {', '.join(others)}" if others else "CLEAN PATH"
        table_data.append([node, status])

    if table_data:
        tbl = Table(table_ax, bbox=[0, 0, 1, 1])
        n_rows = len(table_data)
        tbl.add_cell(0, 0, 0.3, 0.1, text="Favourite", loc='center', facecolor=COLOUR_FAVOURITE, edgecolor='white')
        tbl.add_cell(0, 1, 0.7, 0.1, text="Status", loc='center', facecolor=COLOUR_FAVOURITE, edgecolor='white')
        for i, (name, status) in enumerate(table_data, start=1):
            cell_name = tbl.add_cell(i, 0, 0.3, 0.08, text=name, loc='center', facecolor=COLOUR_BG, edgecolor='gray')
            cell_status = tbl.add_cell(i, 1, 0.7, 0.08, text=status, loc='left', facecolor=COLOUR_BG, edgecolor='gray')
            if "CONFLICT" in status:
                cell_status.get_text().set_color(COLOUR_CONFLICT)
            else:
                cell_status.get_text().set_color(COLOUR_LABEL)
            cell_name.get_text().set_color(COLOUR_LABEL)
            cell_name.get_text().set_fontsize(8)
            cell_status.get_text().set_fontsize(8)

        tbl.auto_set_font_size(False)
        tbl.set_fontsize(8)
        table_ax.add_table(tbl)
        table_ax.set_title("Path check results", color=COLOUR_LABEL, fontsize=10, pad=10)
    else:
        table_ax.text(0.1, 0.5, "No favourite nodes", color=COLOUR_LABEL, fontsize=10)

    # Legend
    legend_elements = [
        mpatches.Patch(color=COLOUR_FAVOURITE, label="Favourite friend"),
        mpatches.Patch(color=COLOUR_REGULAR,   label="Regular friend"),
        mpatches.Patch(facecolor='none', edgecolor=COLOUR_OK, label="No conflict (green border)"),
        mpatches.Patch(facecolor='none', edgecolor=COLOUR_CONFLICT, label="Conflict (red border)"),
    ]
    ax.legend(
        handles=legend_elements,
        loc="upper left",
        facecolor="#2E2E3E",
        edgecolor="#555555",
        labelcolor=COLOUR_LABEL,
        fontsize=9
    )

    ax.set_title("Friends tree – visualizing conflicts on paths to favourites", 
                 color=COLOUR_LABEL, fontsize=14, fontweight="bold", pad=15)
    ax.axis("off")
    plt.tight_layout()
    plt.show()