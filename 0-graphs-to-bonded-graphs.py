import knotpy as kp

#graphs8 = kp.load_diagrams("graphs_abc_8_test.txt", notation="plantri")
#graphs7 = kp.load_diagrams("graphs_abc_7_test.txt", notation="plantri")
#graphs6 = kp.load_diagrams("graphs_abc_6_test.txt", notation="plantri")
#graphs5 = kp.load_diagrams("graphs_abc_5_test.txt", notation="plantri")
#graphs4 = kp.load_diagrams("graphs_abc_4_test.txt", notation="plantri")
#graphs3 = kp.load_diagrams("graphs_abc_3_test.txt", notation="plantri")
graphs3 = kp.load_diagrams("3_vertex_abc.txt", notation="plantri")
graphs4 = kp.load_diagrams("4_vertex_abc.txt", notation="plantri")
graphs5 = kp.load_diagrams("5_vertex_abc.txt", notation="plantri")
graphs6= kp.load_diagrams("6_vertex_abc.txt", notation="plantri")
graphs7= kp.load_diagrams("7_vertex_abc.txt", notation="plantri")
graphs8= kp.load_diagrams("8_vertex_abc.txt", notation="plantri")
all_graphs = (graphs3+graphs4+graphs5+graphs6+graphs7+graphs8)
        #graphs6 + graphs5 + graphs4)

good_graphs = set()

def is_bonded_graph(graph):
    deg_seq = kp.degree_sequence(h)
    n4 = deg_seq.count(4)
    n3 = deg_seq.count(3)
    if len(deg_seq) != n3 + n4:
        return False
    if n3 % 2 != 0:
        return False
    return True


# parallellize arcs
for g in all_graphs:
    print(g)


    sprotne = {g, }

    while len(sprotne) > 0:
        h = sprotne.pop()
        if is_bonded_graph(h):
            good_graphs.add(h)

        deg_seq = kp.degree_sequence(h)
        if max(deg_seq) > 4:
            continue

        for arc in h.arcs:
            ep1, ep2 = arc
            if g.degree(ep1.node) not in [2, 3] or g.degree(ep2.node) not in [2, 3]:
                continue
            h_ = kp.canonical(kp.parallelize_arc(h, arc, inplace=False))

            sprotne.add(h_)

good_graphs = list(good_graphs)
good_graphs = sorted(good_graphs, key=len)
kp.save_diagrams("planar_bonded_graphs.txt", good_graphs)
kp.export_pdf(good_graphs, "planar_bonded_graphs.pdf")