import customtkinter as ctk
from openpyxl import load_workbook
from tkinter import messagebox


window = ctk.CTk()
window.title("Boma Investment and resources LTD")
window.configure(height=500, width=500, padx=20, pady=20)

wb = load_workbook("customtk/boma_data.xlsx")
ws = wb.active

drinks = {
    'big_coke': [5600.0, 20, 'coca_cola'],
    'hero': [6200.0, 20, 'premium_brew'],
    'trophy': [6200.0, 0, 'premium_brew'],
    'tiger': [10200.0, 0, 'nbl'],
    'life': [6200.0, 80, 'nbl'],
    'star': [7400.0, 30, 'nbl'],
    'amstel': [10200.0, 20, 'nbl'],
    'gulder': [7400.0, 0, 'nbl'],
    'desperados': [12200.0, 0, 'nbl'],
    'heineken': [8400.0, 0, 'nbl'],
    'm_stout': [11400.0, 0, 'guinness'],
    's_stout': [12600.0, 0, 'guinness'],
    'maltina': [10200.0, 0, 'nbl'],
    'big_legend': [7800.0, 0, 'nbl'],
    'radler': [9000.0, 0, 'nbl'],
    'flying_fish': [11500.0, 0, 'premium_brew'],
    'budweiser': [7500.0, 10, 'premium_brew'],
}

drinks_lst = list(drinks.keys())
labels_list = []

def show_products():
    global entries
    entries_list = list(entries.values())
    for item in entries_list:
        entry_row = entries_list.index(item)+2
        item.grid(column=2, row=entry_row)
    big_coke.grid(column=0, row=2)
    hero.grid(column=0, row=3)
    trophy.grid(column=0, row=4)
    tiger.grid(column=0, row=5)
    life.grid(column=0, row=6)
    star.grid(column=0, row=7)
    amstel.grid(column=0, row=8)
    gulder.grid(column=0, row=9)
    desperados.grid(column=0, row=10)
    heineken.grid(column=0, row=11)
    m_stout.grid(column=0, row=12)
    s_stout.grid(column=0, row=13)
    maltina.grid(column=0, row=14)
    big_legend.grid(column=0, row=15)
    radler.grid(column=0, row=16)
    flying_fish.grid(column=0, row=17)
    budweiser.grid(column=0, row=18)

    calculator.grid(column=0, row=20, pady=5)
    enter_quantity.grid(column=2, row=1)
    price.grid(column=1, row=1)
    total.grid(column=2, row=20, columnspan=2)
    clearr.grid(column=1, row=20, padx=5)
    customer_name.grid(column=1, row=0, columnspan=2)
    customer_name.insert(0, "Enter customer name here.")
    customer_name.focus()
    customer_label.grid(column=0, row=0)
    for guv in entries:
        txt = drinks[guv][0]
        drink_list = list(drinks.keys())
        label = ctk.CTkLabel(window, text=f"₦{txt}", width=10)
        labels_list.append(label)
        guv_row = drink_list.index(guv) + 2
        label.grid(column=1, row=guv_row)
    header.grid_forget()
    chk_stk.grid_forget()
    save.grid(column=2, row=22, padx=5)
    back_btn.grid(column=0, row=22)
    close.grid_forget()


def save_sale_record():
    customer = customer_name.get()
    brands = []
    quantities = []
    ind_tots = []
    grand_total = 0
    for key in entries:
        quantity = entries[key]
        try:
            quantity = float(quantity.get())
        except ValueError:
            quantity = 0
        else:
            brand = key
            item_price = drinks[brand][0]
            brand_total = item_price * quantity
            ind_tots.append(brand_total)
            brands.append(brand)
            quantities.append(quantity)
    for item in ind_tots:
        grand_total += item
    first_row = [customer]
    # List containing brands, quantities and individual totals for the latest purchase 
    contents_files = []
    for item1, item2, item3 in zip(brands, quantities, ind_tots):
        # Individually adds each item purchased with quantity and item's total 
        contents_row = ['', item1, item2, item3]
        contents_files.append(contents_row)
    last_row = ['Grand total', '', '', '', grand_total]
    new = [
        # Adds latest customer name to next available line on the excel data file
        first_row,
    ]
    for n in contents_files:
        new.append(n)
    new.append(last_row)
    for row in new:
        ws.append(row)
    save_record = messagebox.askokcancel(title="Save entries?", message="Would you like to save this transaction?")
    if save_record:
        wb.save("customtk/boma_data.xlsx")



individual_total_labels = []


def calculate():
    global individual_total_labels
    individual_total_labels = []
    grand_total = 0
    individual_totals = {}
    for drink in entries:
        item_entry = entries[drink]
        item = drink
        item_price = drinks[item][0]
        try:
            item_qty = float(item_entry.get())
        except ValueError:
            item_qty = 0
            item_total = item_qty * item_price
            individual_totals[item] = item_total
        else:
            item_total = item_qty * item_price
            individual_totals[item] = item_total
            grand_total += item_total
    grand_total = format(grand_total, ",")
    total.configure(text=f"Total: ₦{grand_total}0")
    ind_tots_keys = list(individual_totals.keys())
    for item in individual_totals:
        actual_total = format(individual_totals[item], ",")
        label = ctk.CTkLabel(window, text=f"₦{actual_total}0", )
        individual_total_labels.append(label)
        item_row = ind_tots_keys.index(item) + 2
        label.grid(column=3, row=item_row)


def clear():
    global individual_total_labels
    for label in individual_total_labels:
        label.configure(text=f"₦0.00")
    for items in entries:
        drink = items
        entries[drink].delete(0, ctk.END)
        total.configure(text="₦0.00")
    customer_name.delete(0, ctk.END)
    customer_name.focus()

randos_net = []
def check_stock():
    global randos_net
    header.grid_forget()
    our_products.grid_forget()
    chk_stk.grid_forget()
    close.grid_forget()
    for n in drinks:
        src_row = drinks_lst.index(n)
        brand = ctk.CTkButton(window, text=f"{n}")
        brand.grid(column=0, row=src_row)
        randos_net.append(brand)
    for n in drinks:
        stock_qty = drinks[n][1]
        src_row = drinks_lst.index(n)
        qty = ctk.CTkLabel(window, text=f"{stock_qty}")
        qty.grid(column=1, row=src_row)
        randos_net.append(qty)
    bk_btn.grid(column=0, row=24)

def back_products():
    global drink_labels, labels_list
    our_products.grid_forget()
    our_products.grid(column=0, row=1)
    header.grid(column=0, row=0, columnspan=3)
    chk_stk.grid(column=0, row=2)
    close.grid(column=0, row=3)
    for n in drink_labels:
        n.grid_forget()
    for n in entries:
        entries[n].grid_forget()
    for n in buttons:
        n.grid_forget()
    for n in labels_list:
        n.grid_forget()
    customer_name.grid_forget()
    for n in individual_total_labels:
        n.grid_forget()


def back_check_stock():
    global randos_net
    header.grid(column=0, row=0, columnspan=3)
    our_products.grid(column=0, row=1, pady=10)
    chk_stk.grid(column=0, row=2)
    close.grid(column=0, row=3)
    for n in randos_net:
        n.grid_forget()
    bk_btn.grid_forget()


header = ctk.CTkLabel(window, text="BOMA INVESTMENT AND RESOURCES NIG LTD")
header.grid(column=0, row=0, columnspan=3)
chk_stk = ctk.CTkButton(window, text="Check stock", command=check_stock)
chk_stk.grid(column=0, row=2)
our_products = ctk.CTkButton(window, width=9, text="Our products", command=show_products, )
our_products.grid(column=0, row=1, pady=10)
calculator = ctk.CTkButton(window, text="Calculate", command=calculate)
clearr = ctk.CTkButton(window, text="Clear", command=clear)
save = ctk.CTkButton(window, text="save", command=save_sale_record)
back_btn = ctk.CTkButton(window, text="Back", command=back_products)
bk_btn = ctk.CTkButton(window, text="Back", command=back_check_stock)
buttons = [calculator, clearr, save, back_btn, bk_btn]
close = ctk.CTkButton(window, text="Close", command=window.quit)
close.grid(column=0, row=3, pady=10)
# save.configure(pady=5)

# Product ctk.CTkLabels
enter_quantity = ctk.CTkLabel(window, text="Enter Quantity", width=15)
price = ctk.CTkLabel(window, text="Price", width=10)
life = ctk.CTkLabel(window, text="Life", width=10)
star = ctk.CTkLabel(window, text="Star", width=10)
amstel = ctk.CTkLabel(window, text="Amstel", width=10)
gulder = ctk.CTkLabel(window, text="Gulder", width=10)
tiger = ctk.CTkLabel(window, text="Tiger", width=10)
desperados = ctk.CTkLabel(window, text="Desperados", width=10)
heineken = ctk.CTkLabel(window, text="Heineken", width=10)
maltina = ctk.CTkLabel(window, text="Maltina", width=10)
big_legend = ctk.CTkLabel(window, text="Big Legend", width=10)
radler = ctk.CTkLabel(window, text="Star Radler", width=10)
hero = ctk.CTkLabel(window, text="Hero", width=10)
trophy = ctk.CTkLabel(window, text="Trophy", width=10)
big_coke = ctk.CTkLabel(window, text="50cl", width=10)
m_stout = ctk.CTkLabel(window, text="M/stout", width=10)
s_stout = ctk.CTkLabel(window, text="S/stout", width=10)
budweiser = ctk.CTkLabel(window, text="Budweiser", width=10)
flying_fish = ctk.CTkLabel(window, text="Flying fish", width=10)

customer_label = ctk.CTkLabel(window, text="Customer", width=20)
total = ctk.CTkButton(window, text=f"Total: ₦0.00", width=20)
drink_labels = [enter_quantity, price, life, star, amstel, gulder, tiger, desperados, heineken, maltina, big_legend, radler, hero, trophy, big_coke, m_stout, s_stout, budweiser, flying_fish, customer_label, total]

# Entries
customer_name = ctk.CTkEntry(window)
life_entry = ctk.CTkEntry(window)
star_entry = ctk.CTkEntry(window)
amstel_entry = ctk.CTkEntry(window)
gulder_entry = ctk.CTkEntry(window)
tiger_entry = ctk.CTkEntry(window)
desperados_entry = ctk.CTkEntry(window)
heineken_entry = ctk.CTkEntry(window)
maltina_entry = ctk.CTkEntry(window)
big_legend_entry = ctk.CTkEntry(window)
radler_entry = ctk.CTkEntry(window)
hero_entry = ctk.CTkEntry(window)
trophy_entry = ctk.CTkEntry(window)
big_coke_entry = ctk.CTkEntry(window)
m_stout_entry = ctk.CTkEntry(window)
s_stout_entry = ctk.CTkEntry(window)
budweiser_entry = ctk.CTkEntry(window)
flying_fish_entry = ctk.CTkEntry(window)

entries = {
    "big_coke": big_coke_entry,
    "hero": hero_entry,
    "trophy": trophy_entry,
    "tiger": tiger_entry,
    "life": life_entry,
    "star": star_entry,
    "amstel": amstel_entry,
    "gulder": gulder_entry,
    "desperados": desperados_entry,
    "heineken": heineken_entry,
    "m_stout": m_stout_entry,
    "s_stout": s_stout_entry,
    "maltina": maltina_entry,
    "big_legend": big_legend_entry,
    "radler": radler_entry,
    "flying_fish": flying_fish_entry,
    "budweiser": budweiser_entry,

}


window.mainloop()