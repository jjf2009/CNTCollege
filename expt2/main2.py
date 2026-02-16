from prettytable import PrettyTable
import matplotlib.pyplot as plt

def show_table_matplotlib(myTable, title=None):
    headers = myTable.field_names
    rows = [[str(x) for x in row] for row in myTable._rows]
    
    fig, ax = plt.subplots(figsize=(max(8, 1.5*len(headers)), max(3, 0.5*len(rows) + 1.5)))
    ax.axis('off')
    
    if title:
        ax.set_title(title, color='#2c3e50', fontsize=14, weight='bold', pad=20)
    
    # Color scheme
    header_color = "#3498db"
    header_text_color = "white"
    row_colors = ["#ecf0f1", "#ffffff"]
    
    cell_colours = [[row_colors[i % 2] for _ in headers] for i in range(len(rows))]
    
    tbl = ax.table(cellText=rows, colLabels=headers, cellColours=cell_colours,
                   cellLoc='center', loc='center')
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(11)
    tbl.scale(1, 1.8)
    
    # Style header cells
    for key, cell in tbl.get_celld().items():
        row_idx, col_idx = key
        if row_idx == 0:  # Header row
            cell.set_facecolor(header_color)
            cell.set_text_props(color=header_text_color, weight='bold', size=12)
            cell.set_edgecolor('#2c3e50')
            cell.set_linewidth(1.5)
        else:  # Body cells
            cell.set_edgecolor('#bdc3c7')
            cell.set_linewidth(0.8)
            cell.set_text_props(color='#2c3e50', size=10)
    
    plt.tight_layout()
    plt.show()

# --- Simple GCD with PrettyTable + matplotlib display ---
print("=" * 50)
print("EUCLIDEAN ALGORITHM - GCD")
print("=" * 50)

a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))

myTable = PrettyTable(['q', 'r1', 'r2', 'r'])
myTable.align = 'c'

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

print("\n" + str(myTable))
print(f"\n✓ GCD({a}, {b}) = {result}")
print("=" * 50)

show_table_matplotlib(myTable, title=f"Euclidean Algorithm: GCD({a}, {b}) = {result}")

# --- Extended GCD with PrettyTable + matplotlib display ---
print("\n" + "=" * 50)
print("EXTENDED EUCLIDEAN ALGORITHM")
print("=" * 50)

a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))

myTable2 = PrettyTable(['q', 'r1', 'r2', 'r', 's1', 's2', 's', 't1', 't2', 't'])
myTable2.align = 'c'

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
        myTable2.add_row([q, r1, r2, r, s1, s2, s, t1, t2, t])
        r1, r2 = r2, r
        s1, s2 = s2, s
        t1, t2 = t2, t
    
    gcd = r1
    s = s1
    t = t1
    return gcd, s, t

result, x, y = extended_gcd(a, b)

print("\n" + str(myTable2))
print(f"\n✓ Result: {a}({x}) + {b}({y}) = {result}")
print(f"  x = {x}")
print(f"  y = {y}")
print("=" * 50)

show_table_matplotlib(myTable2, title=f"Extended Euclidean Algorithm: {a}x + {b}y = {result}")