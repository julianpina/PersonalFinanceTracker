#Final Project Extra Module

def displayAmount(value):
    """Formats a number to look like money, for example 1000 will become $1000.00."""
    return "${:,.2f}".format(value)
