inventory = [
    # name,       category,   unit_price, units_sold, units_left
    ["Strawberry", "Fruit",      3.50,        40,          10],
    ["Broccoli",   "Vegetable",  2.20,        25,           8],
    ["Cheddar",    "Dairy",      5.00,        18,           4],
    ["Baguette",   "Bakery",     2.80,        35,           2],
    ["Blueberry",  "Fruit",      4.00,        22,           6],
    ["Spinach",    "Vegetable",  1.80,        30,          12],
    ["Yogurt",     "Dairy",      1.20,        50,          15],
    ["Croissant",  "Bakery",     3.00,        28,           3],
]

for item in inventory:
    name, category, unit_price, units_sold, units_left = item
    print(f"Item: {name}, Category: {category}, Unit Price: ${unit_price:.2f}, Units Sold: {units_sold}, Units Left: {units_left}")

tot_rev = 0
for i in inventory:
    tot_rev += unit_price * units_sold
print(f'Total Revenue: {tot_rev}')

for item in inventory:
    name, category, unit_price, units_sold, units_left = item
    if units_left<5:
        print({name})

for items in inventory:
    name,category,unit_price,units_sold,unit_left = items
    revenue=unit_price*units_sold
    print(f"category : {category}  totalrevenue : {revenue}")