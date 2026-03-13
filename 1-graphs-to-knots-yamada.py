from typing import Any

import knotpy as kp
from collections import defaultdict

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
all_graphs = kp.load_diagrams("planar_bonded_graphs.txt")
#graphs_2 = kp.load_diagrams("graphs_abc_2.txt", notation="plantri")
#graphs_3 = kp.load_diagrams("graphs_abc_3.txt", notation="plantri")

print("Loaded", len(all_graphs), "graphs")

knots = []
for g in all_graphs:
    for k in kp.vertices_to_crossings(g, all_crossing_signs=True):
        knots.append(k)

print("Good bonded knots", len(knots))
kp.save_diagrams("all_bonded_knots.txt", knots)

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
kp.save_diagrams("all_canonical_bonded_knots.txt", canonical_knots)


kp.export_pdf(list(canonical_knots)[:50], "all-bonded-canonical-knots_50.pdf", ignore_errors=True)

#knots_not_connected_sums = [k for k in canonical_knots if not kp.is_connected_sum(k)]
#print("knots without connected sums", len(knots_not_connected_sums))

#kp.save_diagrams("all_knots_not_connected_sums.txt", knots_not_connected_sums )

#kp.export_pdf(knots_not_connected_sums, "all_knots_not_connected_sums.pdf")



#!!
yamada_polys = [kp.yamada(k, True) for k in canonical_knots]
print("Done with yamada polys")
# preveri yamadas eq

groups = defaultdict(list)

for p, g in zip(yamada_polys, canonical_knots):
    groups[p].append(g)

# UNIQUE KNOTS
unique_knots = [g[0] for g in groups.values() if len(g) == 1]
print("unique (all):", len(unique_knots))
unique_knots = sorted(unique_knots, key=len)

#kp.export_pdf(unique_knots, "unique_part_1_sums_unions.pdf")

unique_knots_good = set()
bad_knots = []

#for k in unique_knots:
   # if not kp.is_connected_sum(k) and not kp.is_disjoint_union(k):
        #unique_knots_good.add(k)


print("unique (non-composite):", len(unique_knots_good))
kp.save_diagrams("unique_knots_1.txt", unique_knots)
kp.export_pdf(unique_knots, "unique_1.pdf")

# NON-UNIQUE KNOTS
non_unique_knots = [g for g in groups.values() if len(g) > 1]

kp.save_diagram_sets("non_unique_knots_1.txt", non_unique_knots)

#
#non_unique_graphs = [g for graphs in non_unique_graphs for g in graphs]
#kp.save_diagrams("non_unique_graphs_saved.txt", non_unique_graphs)  # shrani


print("unique knots", len(unique_knots_good))
print("non unique knot groups", len(non_unique_knots), "containing", sum(len(g) for g in non_unique_knots), "knots")

