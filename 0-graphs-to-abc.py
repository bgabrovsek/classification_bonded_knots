import knotpy as kp


def num_to_char(n: int) -> str:
    """Convert 1 -> 'a', 2 -> 'b', ..."""
    return chr(ord('a') + n - 1)

def process_line(line: str) -> str:
    # Remove leading ID (everything before the first colon)
    if ":" in line:
        line = line.split(":", 1)[1].strip()

    output_chars = []

    import re
    # Find patterns like 1[2  3  4  5]
    blocks = re.findall(r'\d+\[([0-9\s]+)\]', line)

    for block in blocks:
        # Get numbers inside the brackets
        nums = block.split()
        # Convert each to a letter
        chars = ''.join(num_to_char(int(n)) for n in nums)
        output_chars.append(chars)

    # Return them joined by a space, or however you want them formatted
    return ' '.join(output_chars)

def process_file(infile: str, outfile: str):
    with open(infile, 'r') as f_in, open(outfile, 'w') as f_out:
        for line in f_in:
            result = process_line(line).replace(" ", ",")
            f_out.write(result + "\n")


process_file("graphs10.txt", "graphs_abc_10.txt")