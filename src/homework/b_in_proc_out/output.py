def multiply_numbers(a, b):
    """
    Returns the product of two numbers.
    """
    return a * b
  
    # Named constant: sales tax rate 6.75%
TAX_RATE: float = 0.0675

def get_sales_tax_amount(meal_amount: float) -> float:
    """Return sales tax for meal_amount using TAX_RATE (6.75%)."""
    return meal_amount * TAX_RATE

def get_tip_amount(meal_amount: float, tip_rate: float) -> float:
    """
    Return tip amount.
    tip_rate is a decimal (e.g., 0.15 for 15%).
    """
    return meal_amount * tip_rate
