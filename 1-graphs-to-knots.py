import knotpy as kp

# generiramo vse grafe z 2,... 7/8 vozlišč
# združimo v eno tabelo
# dobre (deg <= 4, sodo deg=3) ohranimo
# simplify + canonical
# odstranimo connected sums
# yamada
# bonded knote, ki imajo enolične yamade, shranimo (so že del klasifikacije)
# bonded knote, ki si delijo yamado, poenostavimo: simplify depth = 1, depth=2,.. + preverimo connected sum

# knots = [k for k in knots if not kp.is_connected_sum(k)]


# n = 2,3,4,5,6,7, 8?
graphs_10 = kp.load_diagrams("graphs_abc_10.txt", notation="plantri")
#graphs_2 = kp.load_diagrams("graphs_abc_2.txt", notation="plantri")
#graphs_3 = kp.load_diagrams("graphs_abc_3.txt", notation="plantri")
"""
...

"""
all_graphs = graphs_10 #+ graphs_2 + graphs_3

print("Loaded", len(graphs_10), "graphs")




good_graphs = []
for g in graphs_10:
    d = kp.degree_sequence(g)
    if max(d) <= 4 and min(d) >= 3:
        if sum([1 for n in d if n == 3]) % 2 == 0:
            good_graphs.append(g)

print("Good graphs", len(good_graphs))

kp.save_diagrams("1-good_graphs.txt", good_graphs)

kp.export_pdf(good_graphs[:5], "1-good_graphs_ex.pdf")

knots = []
for g in good_graphs:
    for k in kp.vertices_to_crossings(g, all_crossing_signs=True):
        knots.append(k)

print("Good bonded knots", len(knots))
kp.save_diagrams("1-all_bonded_knots.txt", knots)

canonical_knots = set()
for k in kp.bar(knots):
    #k = kp.simplify(k, depth=0)
    k = kp.simplify_decreasing(k)  # greedy
    k = kp.canonical(k)
    canonical_knots.add(k)

#Good bonded knots 46981
#kp.is_connected_sum(k)



"""

"""

print("Canonical bonded knots", len(canonical_knots))
kp.save_diagrams("1-all_canonical_bonded_knots.txt", canonical_knots)


kp.export_pdf(list(canonical_knots)[:50], "1-bonded-canonical-knots.pdf", ignore_errors=True)
