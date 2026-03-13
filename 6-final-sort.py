import knotpy as kp
from knotpy import connected_sum, disjoint_union

bonded_group_1 = kp.load_diagram_sets("unique_knots_1.txt")
bonded_group_2 = kp.load_diagram_sets("unique_knots_2.txt")
bonded_group_3 = kp.load_diagram_sets("unique_knots_3.txt")
bonded_group_4 = kp.load_diagram_sets("unique_knots_4.txt")
bonded_group_5 = kp.load_diagram_sets("unique_knots_5.txt")
non_unique_bonded_group = kp.load_diagram_sets("non_unique_knots_5.txt")
bonded_group_6=[]
non_unique_bonded_group = [
    g for group in non_unique_bonded_group for g in group
]
for g in non_unique_bonded_group:
    if not kp.is_connected_sum(g) and not kp.is_disjoint_union(g):
        bonded_group_6.append(g)


table_1=bonded_group_1+bonded_group_2+bonded_group_3+bonded_group_4+bonded_group_5
table=[]
table_1 = [
g for group in table_1 for g in group
]
for g in table_1:
    if not kp.is_connected_sum(g) and not kp.is_disjoint_union(g):
        table.append(g)

final_unique_1 = sorted(bonded_group_6, key=len)
del final_unique_1[3:5]

kp.save_diagrams("final_unique_1.txt", final_unique_1)
kp.export_pdf(final_unique_1, "final_unique_1.pdf")

final_unique_2 = sorted(table, key=len)
kp.save_diagrams("final_unique_2.txt", final_unique_2)
kp.export_pdf(final_unique_2, "final_unique_2.pdf")

final_unique_with_knots_1=final_unique_1+final_unique_2
final_unique_with_knots = sorted(final_unique_with_knots_1, key=len)

final_unique=[]
for g in final_unique_with_knots:
    if not kp.is_knot(g) and not kp.is_link(g):
        final_unique.append(g)

kp.save_diagrams("final_unique_with_knots.txt", final_unique_with_knots)
kp.export_pdf(final_unique_with_knots, "final_unique_with_knots.pdf")

kp.save_diagrams("final_unique.txt", final_unique)
kp.export_pdf(final_unique, "final_unique.pdf")