def remove_duplicate_customers(customers):
    unique_customers = set(customers)

    print("Unique customer records:")
    for customer in unique_customers:
        print(customer)

customers = [
    ('Amit Sharma', 'amit@example.com'),
    ('Neha Singh', 'neha@example.com'),
    ('Amit Sharma', 'amit@example.com'),  # Duplicate
    ('Ravi Kumar', 'ravi@example.com'),
    ('Priya Iyer', 'priya@example.com'),
    ('Neha Singh', 'neha@example.com')  # Duplicate
]

remove_duplicate_customers(customers)
