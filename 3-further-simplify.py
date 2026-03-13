import knotpy as kp
from collections import defaultdict

bonded_groups_1 = kp.load_diagram_sets("non_unique_knots_2.txt")
bonded_groups_2_base = []

print("Reducing")
for group in kp.bar(bonded_groups_1):
    non_unique_group = set(kp.reduce_equivalent_diagrams(group, depth=2))
    bonded_groups_2_base.append(non_unique_group)

print("done")


#bonded_groups_2 = []
#bad_knots = []
#for group in bonded_groups_2_base:
    #new_group = set()
    #for k in group:
     #   if not kp.is_connected_sum(k) and not kp.is_disjoint_union(k):
       #     new_group.add(k)
      #  else:
       #     bad_knots.append(k)
    #bonded_groups_2.append(new_group)

#kp.export_pdf(bad_knots, "bad_knots_3.pdf")
unique_3 = [g.pop() for g in bonded_groups_2_base if len(g) == 1]
non_unique_3 = [g for g in bonded_groups_2_base if len(g)>= 2]


#unique_5 = set()
#unique_5_composite = set()


# for k in unique_4:
    #if not kp.is_connected_sum(k) and not kp.is_disjoint_union(k):
       # unique_5.add(k)
    #else:
        #unique_5_composite.add(k)

print("unique (all):", len(unique_3)), #"non-composite:", len(unique_5), "composite:", len(unique_5_composite))
print("non-unique (all):", len(non_unique_3), "containing")

unique_3 = sorted(unique_3, key=len)
kp.save_diagrams("unique_knots_3.txt", unique_3)
kp.export_pdf(unique_3, "unique_3.pdf")
#kp.export_pdf(unique_5_composite, "unique_3_composite.pdf")
kp.save_diagram_sets("non_unique_knots_3.txt", non_unique_3)

import os

os.makedirs("slike_2", exist_ok=True)
for i, group in enumerate(non_unique_3):
    kp.export_pdf(group, "slike_2\\3_group_" + str(i)  +".pdf")

exit()