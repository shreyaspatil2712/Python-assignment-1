def clean_product_list(pid):
    if not pid:
        return []

    unique_pid = set(pid)

    cleaned_product_list = sorted(unique_pid)

    return cleaned_product_list

pid = [102, 204, 102, 153, 204, 187, 153]
print(clean_product_list(pid))
