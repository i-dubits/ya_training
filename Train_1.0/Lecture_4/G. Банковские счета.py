with (open('input.txt', 'r') as f):
    cust_dict = {}
    while True:
        line = f.readline().strip().split()
        if line:
            operation_type = line[0]
            if operation_type == 'DEPOSIT':
                name, sum = line[1], int(line[2])
                if name in cust_dict:
                    cust_dict[name] += sum
                else:
                    cust_dict[name] = sum

            elif operation_type == 'WITHDRAW':
                name, sum = line[1], int(line[2])
                if name in cust_dict:
                    cust_dict[name] -= sum
                else:
                    cust_dict[name] = -sum

            elif operation_type == 'BALANCE':
                name =  line[1]
                if name in cust_dict:
                    print(f'{cust_dict[name]}')
                else:
                    print('ERROR')

            elif operation_type == 'TRANSFER':
                name_from, name_to, sum = line[1], line[2], int(line[3])
                if name_from in cust_dict:
                    if name_to in cust_dict:
                        cust_dict[name_from] -= sum
                        cust_dict[name_to] += sum
                    else:
                        cust_dict[name_from] -= sum
                        cust_dict[name_to] = sum
                else:
                    if name_to in cust_dict:
                        cust_dict[name_from] = -sum
                        cust_dict[name_to] += sum
                    else:
                        cust_dict[name_from] = -sum
                        cust_dict[name_to] = sum

            elif operation_type == 'INCOME':
                p = int(line[1])
                for client_name in cust_dict.keys():
                    if cust_dict[client_name] > 0:
                        cust_dict[client_name] = int(cust_dict[client_name]*(1 + 0.01*p))
        else:
            break

