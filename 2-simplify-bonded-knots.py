from operator import truediv
from typing import Any

import knotpy as kp

#### NOV PROGRAM

# shraniš unique
# shraniš non-unique

bonded_groups_1 = kp.load_diagram_sets("non_unique_knots_1.txt")
bonded_groups_2_base = []

print("Reducing")
for group in kp.bar(bonded_groups_1):
    print("len", len(group))
    non_unique_group = set(kp.reduce_equivalent_diagrams(group, depth=1))
    bonded_groups_2_base.append(non_unique_group)

print("done")


#bonded_groups_2 = []
#bad_knots = []
#for group in bonded_groups_2_base:
    #new_group = set()
    #for k in group:
        #if not kp.is_connected_sum(k) and not kp.is_disjoint_union(k):
            #new_group.add(k)
        #else:
            #bad_knots.append(k)
    #bonded_groups_2.append(new_group)

#kp.export_pdf(bad_knots, "bad_knots_2.pdf")
unique_2 = [g.pop() for g in bonded_groups_2_base if len(g) == 1]
non_unique_2 = [g for g in bonded_groups_2_base if len(g)>= 2]


#unique_3 = set()
#unique_3_composite = set()


#for k in unique_2:
    #if not kp.is_connected_sum(k) and not kp.is_disjoint_union(k):
        #unique_3.add(k)
   # else:
       # unique_3_composite.add(k)

#print("unique (all):", len(unique_2), "non-composite:", len(unique_3), "composite:", len(unique_3_composite))
## print("non-unique (all):", len(non_unique_2), "containing")##

unique_2 = sorted(unique_2, key=len)
kp.save_diagrams("unique_knots_2.txt", unique_2)
kp.export_pdf(unique_2, "unique_2.pdf")
#kp.export_pdf(unique_3_composite, "unique_2_composite.pdf")
kp.save_diagram_sets("non_unique_knots_2.txt", non_unique_2)

import os

os.makedirs("slike", exist_ok=True)
for i, group in enumerate(non_unique_2):
    kp.export_pdf(group, "slike\\2_group_" + str(i)  +".pdf")

exit()

bonded_groups_2 = [[k for k in group if not kp.is_connected_sum(k) and not kp.is_disjoint_union(k)] for group in bonded_groups_2]


unique_2 = [g[0] for g in bonded_groups_2 if len(g) == 1]
non_unique_2 = [g for g in bonded_groups_2 if len(g)>= 2]
unique_canonical_knots: set[Any]=set()
for group in unique_2:

    group = kp.simplify_decreasing(group)  # greedy
    group = kp.simplify(group, depth=3)
    group = kp.canonical(group)
    if not kp.is_connected_sum(group) and not kp.is_disjoint_union(group):
        unique_canonical_knots.add(group)

unique_2 = sorted(unique_2, key=len)
unique_canonical_knots = sorted(unique_canonical_knots, key=len)

kp.save_diagram_sets("non_unique_2.txt", non_unique_2)  # shrani
kp.save_diagrams("unique_2.txt", unique_2 )  # shrani
kp.save_diagrams("unique_canonical_knots.txt", unique_canonical_knots)


kp.export_pdf(unique_2, "unique_part_2.pdf")
kp.export_pdf(unique_canonical_knots, "unique_part_2_canonical.pdf")

kp.export_pdf([k for group in non_unique_2 for k in group], "non_unique_2.pdf")

print("Unique graphs", len(unique_2))
print("Non-unique groups", len(non_unique_2), "containing", sum(len(group) for group in non_unique_2),"knots")

#kp.export_pdf_groups()
#vrne:
#r = {a:[a,c,d], b:[b]}
#r = set(r)  # vzemi samo keys
