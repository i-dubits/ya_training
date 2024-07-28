with (open('input.txt', 'r') as f):
    cust_dict = {}
    while True:
        line = f.readline().strip().split()
        if line:
            cust_name, item_name, price = line[0], line[1], int(line[2])
            if cust_name not in cust_dict:
                cust_dict[cust_name] = {}

            if item_name not in cust_dict[cust_name]:
                cust_dict[cust_name][item_name] = price
            else:
                cust_dict[cust_name][item_name] += price
        else:
            break

customers_ordered = sorted(cust_dict)
for cust_name in customers_ordered:
    print(f'{cust_name}:')
    items_ordered = sorted(cust_dict[cust_name])
    for item_name in items_ordered:
        print(f'{item_name} {cust_dict[cust_name][item_name]}')