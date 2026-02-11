from prettytable import PrettyTable
import matplotlib.pyplot as plt

def show_table_matplotlib(myTable, title=None):
    headers = myTable.field_names
    rows = [[str(x) for x in row] for row in myTable._rows]

    _fig, ax = plt.subplots(figsize=(max(6, 1.0*len(headers)), max(2, 0.4*len(rows) + 1)))
    ax.axis('off')
    if title:
        ax.set_title(title, color='#40466e', fontsize=12, weight='bold')

    # alternating row colors and header color
    header_color = "#40466e"
    header_text_color = "white"
    row_colors = ["#f7fbff", "#ffffff"]
    cell_colours = [[row_colors[i % 2] for _ in headers] for i in range(len(rows))]

    tbl = ax.table(cellText=rows, colLabels=headers, cellColours=cell_colours,
                   cellLoc='center', loc='center')
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(10)
    tbl.scale(1, 1.2)

    # style header cells (only if present)
    for key, cell in tbl.get_celld().items():
        row_idx, col_idx = key
        if row_idx == -1:
            cell.set_facecolor(header_color)
            cell.get_text().set_color(header_text_color)
            cell.get_text().set_weight('bold')

    # style body cells (edges/text color)
    for i in range(len(rows)):
        for j in range(len(headers)):
            if (i, j) in tbl.get_celld():
                cell = tbl[i, j]
                cell.set_edgecolor('#d0d7de')
                cell.set_linewidth(0.6)
                cell.get_text().set_color('#222222')

    plt.tight_layout()
    plt.show()

# --- simple gcd with PrettyTable + matplotlib display ---
a = int(input("Enter Number1:"))
b = int(input("Enter Number2:"))

myTable = PrettyTable(['q', 'r1', 'r2', 'r'])

def gcd(a, b):
    r1 = a
    r2 = b
    while r2 > 0:
        q = r1 // r2
        r = r1 - q * r2
        myTable.add_row([q, r1, r2, r])
        r1, r2 = r2, r
    return r1

result = gcd(a, b)
print(myTable)
show_table_matplotlib(myTable, title=f"Euclidean steps: GCD({a}, {b})")
print(f"GCD({a}, {b}) = {result}")

# --- extended gcd with PrettyTable + matplotlib display ---
a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))

myTable = PrettyTable(['q', 'r1', 'r2', 'r','s1','s2','s','t1','t2','t'])

def extended_gcd(a, b):
    r1 = a
    r2 = b
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1
    while r2 > 0:
        q = r1 // r2
        r = r1 - q * r2
        s = s1 - q * s2
        t = t1 - q * t2
        myTable.add_row([q, r1, r2, r, s1, s2, s, t1, t2, t])
        r1, r2 = r2, r
        s1, s2 = s2, s
        t1, t2 = t2, t
    gcd = r1
    s = s1
    t = t1
    return gcd, s, t

result, x, y = extended_gcd(a, b)
print(myTable)
show_table_matplotlib(myTable, title=f"Extended Euclidean steps: {a}, {b}")
print(f"{a}x+{b}y = {result}")
print(f"x= {x}")
print(f"y= {y}")
