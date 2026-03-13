import knotpy as kp
from collections import defaultdict
from to_latex import *
from sympy import latex

def yamada_math(s):
    if s is None:
        return ""
    return f"${latex(s)}$"


knots = kp.load_diagrams("final_unique_without_mirror.txt")
invariants = {}
names = defaultdict(int)

#kp.export_pdf(knots, "bonded_knots.pdf")


for page, k in enumerate(knots, start=1):
    v = len(k.vertices) # vertices
    b = v // 2  # bonds
    c = len(k.crossings)  # crossings
    l = kp.number_of_link_components(k)  # bonded knotoid or bonded linkoid?

    signature = (v+c, c, b, l)
    y = kp.yamada(k)
    ym = kp.yamada_mirror(y)
    chiral = "chiral" if y != ym else "achiral"
    chiral = y != ym

    names[signature] += 1
    name = str(signature).replace(" ", "") + "_" + str(names[signature])
    k.name = name


    invariants[name] = {
        "diagram":k,
        "em": kp.to_condensed_em_notation(k),
        "pd": kp.to_pd_notation(k),
        "yamada": y,
        "chiralily": chiral,
        "page": page,
        "bonded": kp.is_bonded_knot(k)}

    print(invariants[name])

kp.save_invariant_table("bonded_invariant_table.csv", invariants)

print("saved", len(invariants), "invariants")

####### SAVE LATEX IMAGES TABLE
save_bonded_knots_table_tex(invariants)

#### SAVE LATEX TABLE
save_invariant_tables(invariants)
