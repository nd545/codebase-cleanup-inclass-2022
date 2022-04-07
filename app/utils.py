def to_usd(my_price):
    """
    This is a docstring. It tells us what this function is about.
    What its responsibilities are
    What the parameters are 
    What this function will return
    Example of invoking the function
    """
    return '${:,.2f}'.format(my_price)

    #if this code is in the global scope of a file wer're trying to import from 
    #... it will throw errors when we try to run these
    #price = input("Please chosse a price like 4.9999")
    #print(to_usd(float(price)))

if __name__ == "__main__":
    #nesting code in the main condition will allow other scritps to clearly
    #import function from this file without 
    #if this code is in the global scope of a file wer're trying to import from 
    #... it will throw errors when we try to run these
    price = input("Please choose a price like 4.9999")
    print(to_usd(float(price)))    