# Global tax rates (as decimals)
FICA_RATE = 0.0765
FEDERAL_RATE = 0.08

def get_gross_pay(hours, rate):
    """
    Compute gross pay with overtime at 1.5x over 40 hours.
    Works for nonnegative hours and rate.
    """
    h = float(hours)
    r = float(rate)
    if h <= 40:
        return h * r
    # overtime
    regular = 40 * r
    overtime = (h - 40) * (1.5 * r)
    return regular + overtime

def get_fica_tax(gross_pay):
    """
    Return FICA tax from gross pay using global FICA_RATE.
    """
    g = float(gross_pay)
    return g * FICA_RATE

def get_federal_tax(gross_pay):
    """
    Return Federal tax from gross pay using global FEDERAL_RATE.
    """
    g = float(gross_pay)
    return g * FEDERAL_RATE
