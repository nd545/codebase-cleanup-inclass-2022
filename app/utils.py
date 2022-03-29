def to_usd(my_price):
    """
    This is a docstring. It tells us what this function is about.
    What its responsibilities are
    What the parameters are 
    What this function will return
    Example of invoking the function
    """
    return '${:,.2f}'.format(my_price)

price = input("Please choose a price like 4.9999")

print(to_usd(float(price)))