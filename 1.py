def classifyEdges(g_nodes, g_from, g_to, g_weight):
    c = 0
    d = {}
    for i in range(0, g_nodes):
        while True:
            if g_to[c] < g_from[c]:
                break
            else:
                if (str(g_from[c]) + "->" + str(g_to[c])) in d:
                    d[str(g_from[c]) + "->" + str(g_to[c])] = g_weight[c]