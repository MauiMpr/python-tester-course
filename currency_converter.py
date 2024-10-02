import exchange_rates

def convert_GBP_to_USA(amount):
    return amount * exchange_rates.GBP_to_USA

def convert_GBP_to_SA(amount):
    return amount * exchange_rates.GBP_to_SA

def convert_GBP_to_Canada(amount):
    return amount * exchange_rates.GBP_to_Canada

GBP_amount = 200

USA_amount = convert_GBP_to_USA(GBP_amount)
SA_amount = convert_GBP_to_SA(GBP_amount)
Canada_amount = convert_GBP_to_Canada(GBP_amount)

print(f"GBP {GBP_amount} is equal to :")
print(f"USA - {USA_amount}")
print(f"SA - {SA_amount}")
print(f"Canada - {Canada_amount}")


    