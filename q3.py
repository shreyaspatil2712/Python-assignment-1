def organize_sales_data(sales_data):
    cust_spend = {}


    for name, amount in sales_data:
        if name in cust_spend:
            cust_spend[name] += amount  
        else:
            cust_spend[name] = amount  


    for name in sorted(cust_spend):
        print(f"{name}: {cust_spend[name]}")

sales_data = [
    ('Alice', 200),
    ('Bob', 150),
    ('Alice', 100),
    ('Charlie', 250),
    ('Bob', 50)
]

organize_sales_data(sales_data)
