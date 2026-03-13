from pathlib import Path

from pathlib import Path
import re
def save_bonded_knots_table_tex(invariants, output_tex="bonded-knots-table.tex",
                                pdf_file="bonded_knots.pdf", cols=4):

    output_tex = Path(output_tex)

    # Sort strictly by page number
    items = sorted(invariants.items(), key=lambda kv: kv[1]["page"])

    lines = []
    lines.append(r"\begin{figure}[ht]")
    lines.append(r"\centering")
    lines.append(r"\setlength{\tabcolsep}{8pt}")
    lines.append(r"\renewcommand{\arraystretch}{1.2}")
    lines.append(r"\begin{tabular}{" + "c"*cols + "}")

    for i in range(0, len(items), cols):
        chunk = items[i:i+cols]

        # image row
        img_cells = [
            rf"\includegraphics[page={data['page']},width=0.22\textwidth]{{{pdf_file}}}"
            for name, data in chunk
        ]
        img_cells += [""] * (cols - len(img_cells))
        lines.append(" & ".join(img_cells) + r" \\")

        # name row
        name_cells = [rf"${name}$" for name, data in chunk]
        name_cells += [""] * (cols - len(name_cells))
        lines.append(" & ".join(name_cells) + r" \\")

    lines.append(r"\end{tabular}")
    lines.append(r"\end{figure}")

    output_tex.write_text("\n".join(lines) + "\n", encoding="utf-8")




def tex_escape(s: str) -> str:
    repl = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
    }
    return "".join(repl.get(ch, ch) for ch in str(s))


# convert **k → ^{k}
_pow = re.compile(r"\*\*\s*([+-]?\d+)")
def normalize_powers(s):
    return _pow.sub(r"^{\1}", s).replace("*","")


def yamada_math(s):
    if s is None:
        return ""
    s = str(s).strip()
    if not s:
        return ""
    s = normalize_powers(s)
    return f"${s}$"


def format_name(name):
    m = re.match(r"^(.*)_(\d+)$", name)
    if m:
        a,b = m.groups()
        return f"${a}_{{{b}}}$"
    return f"${name}$"


def format_chirality(v):
    s = str(v).lower()
    if s in ("true","1","yes"):
        return "chiral"
    if s in ("false","0","no"):
        return "achiral"
    return "unknown"

def format_bonded(v):
    s = str(v).lower()
    if s in ("true","1","yes"):
        return "yes"
    if s in ("false","0","no"):
        return "no"
    return "no"

def save_invariant_tables(invariants, output="bonded_tables.tex"):

    items = sorted(invariants.items(), key=lambda kv: kv[1]["page"])

    lines = []

    # ---------- TABLE 1 ----------
    lines.append(r"\begin{table}[h]")
    lines.append(r"\centering")
    lines.append(r"\begin{tabular}{llll}")
    lines.append(r"\hline")
    lines.append(r"Name & Chirality & Bonded & Yamada \\")
    lines.append(r"\hline")

    for name,data in items:
        name_tex = format_name(name)
        chir = format_chirality(data.get("chiralily",data.get("chirality","")))
        yam = yamada_math(data.get("yamada",""))
        bon = format_bonded(data.get("bonded",""))

        lines.append(f"{name_tex} & {chir} & {bon} & {yam} \\\\")

    lines.append(r"\hline")
    lines.append(r"\end{tabular}")
    lines.append(r"\caption{Bonded knots and their Yamada polynomial}")
    lines.append(r"\end{table}")
    lines.append("")


    # ---------- TABLE 2 ----------
    lines.append(r"\begin{table}[h]")
    lines.append(r"\centering")
    lines.append(r"\begin{tabular}{ll}")
    lines.append(r"\hline")
    lines.append(r"Name & PD code \\")
    lines.append(r"\hline")

    for name,data in items:
        name_tex = format_name(name)
        pd = tex_escape(data.get("pd",""))

        lines.append(
            f"{name_tex} & {{\\scriptsize\\ttfamily {pd}}} \\\\"
        )

    lines.append(r"\hline")
    lines.append(r"\end{tabular}")
    lines.append(r"\caption{PD codes of bonded knots}")
    lines.append(r"\end{table}")
    lines.append("")

    Path(output).write_text("\n".join(lines), encoding="utf-8")