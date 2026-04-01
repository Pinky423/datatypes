def product_details(**kwargs):
    total = kwargs["price"] * kwargs["quantity"]
    return total
result = product_details(name="laptop",price=7890,quantity=10)
print("total price",result)